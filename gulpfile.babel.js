/**
 *
 *  Web Starter Kit
 *  Copyright 2015 Google Inc. All rights reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License
 *
 */

'use strict';

// This gulpfile makes use of new JavaScript features.
// Babel handles this without us having to do anything. It just works.
// You can read more about the new JavaScript features here:
// https://babeljs.io/docs/learn-es2015/

import path from 'path';
import gulp from 'gulp';
import del from 'del';
import runSequence from 'run-sequence';
import browserSync from 'browser-sync';
import swPrecache from 'sw-precache';
import gulpLoadPlugins from 'gulp-load-plugins';
import {output as pagespeed} from 'psi';
import pkg from './package.json';
import {stream as wiredep} from 'wiredep';
import postcss from 'gulp-postcss';
import cssnext from 'postcss-cssnext';
import autoprefixer from 'autoprefixer';
import svgSprite from 'gulp-svg-sprite';
import webpack from 'webpack-stream';
import webpackConfig from './webpack.config.js';
// import browserify from 'browserify';
// import babelify from 'babelify';
// import source from 'vinyl-source-stream';
// import buffer from 'vinyl-buffer';

const $ = gulpLoadPlugins();
const reload = browserSync.reload;

console.log($);

// Lint JavaScript
gulp.task('lint', () =>
  gulp.src('unusualbusiness/assets/scripts/**/*.js')
    .pipe($.eslint())
    .pipe($.eslint.format())
    .pipe($.if(!browserSync.active, $.eslint.failOnError()))
);

gulp.task('browserify', function () {
    // app.js is your main JS file with all your module inclusions
    return browserify({entries: './unusualbusiness/assets/scripts/main.js', debug: true})
        .transform("babelify", { presets: ["es2015"] })
        .bundle()
        .pipe(source('main.js'))
        .pipe(buffer())
        .pipe($.sourcemaps.init())
        .pipe($.concat('bundle.min.js'))
        .pipe($.uglify({preserveComments: 'some'}))
        .pipe($.sourcemaps.write('.'))
        .pipe(gulp.dest('unusualbusiness/static/scripts'))
});

gulp.task('webpack', function() {
    return gulp.src( [
        './unusualbusiness/assets/scripts/main.js']
    )
    .pipe(webpack(webpackConfig))
    .pipe(gulp.dest('unusualbusiness/static/scripts'));
});

// Optimize images
gulp.task('images', () =>
  gulp.src([
      'unusualbusiness/assets/images/**/*',
      '!unusualbusiness/assets/images/**/*.svg'
  ]).pipe($.cache($.imagemin({
      progressive: true,
      interlaced: true
    })))
    .pipe(gulp.dest('unusualbusiness/static/images'))
    .pipe($.size({title: 'images'}))
);

// Copy Web Fonts To Dist
gulp.task('fonts', function () {
  return gulp.src(['unusualbusiness/assets/fonts/**'])
    .pipe(gulp.dest('unusualbusiness/static/fonts'))
    .pipe($.size({title: 'fonts'}));
});

//gulp.task('fonts', () => {
//  return gulp.src(require('main-bower-files')('**/*.{eot,svg,ttf,woff,woff2}', function (err) {})
//    .concat('unusualbusiness/assets/fonts/**/*'))
//    .pipe(gulp.dest('.tmp/fonts'))
//    .pipe(gulp.dest('unusualbusiness/static/fonts'));
//});

// Compile and automatically prefix stylesheets
gulp.task('styles', () => {
  const AUTOPREFIXER_BROWSERS = [
    'ie >= 10',
    'ie_mob >= 10',
    'ff >= 30',
    'chrome >= 34',
    'safari >= 7',
    'opera >= 23',
    'ios >= 7',
    'android >= 4.4',
    'bb >= 10'
  ];

    var postcss_processors = [
        cssnext()
        // autoprefixer(AUTOPREFIXER_BROWSERS)
    ];

  return gulp.src([
    'unusualbusiness/assets/styles/**/*.scss',
    'unusualbusiness/static/styles/**/*.css'
    // "unusualbusiness/static/bower_components/Materialize/sass/**/*.scss"
  ])
    .pipe($.newer('.tmp/styles'))
    .pipe($.sourcemaps.init())
    //.pipe($.sourcemaps.write({includeContent:false, sourceRoot:'unusualbusiness/static/bower_components/css-hamburgers/dist/hamburgers.css'})) // inline sourcemap without embedded sources

    .pipe($.sass({}))
    .pipe(postcss(postcss_processors))
    .pipe(gulp.dest('.tmp/styles'))
    // Concatenate and minify styles
    .pipe($.if('*.css', $.cssnano()))
    .pipe($.size({title: 'styles'}))
    .pipe($.sourcemaps.write('./'))
    .pipe(gulp.dest('unusualbusiness/static/styles'));
});


// Scan your HTML for assets & optimize them
gulp.task('html', () => {
  return gulp.src('unusualbusiness/templates/**/*.html')
    .pipe($.useref({searchPath: '{.tmp,app}'}))
    // Remove any unused CSS
    .pipe($.if('*.css', $.uncss({
      html: [
        'unusualbusiness/templates/**/*.html'
      ],
      // CSS Selectors for UnCSS to ignore
      ignore: []
    })))

    // Concatenate and minify styles
    // In case you are still using useref build blocks
    .pipe($.if('*.css', $.cssnano()))

    // Minify any HTML
//    .pipe($.if('*.html', $.htmlmin({
//      removeComments: true,
//      collapseWhitespace: true,
//      collapseBooleanAttributes: true,
//      removeAttributeQuotes: true,
//      removeRedundantAttributes: true,
//      removeEmptyAttributes: true,
//      removeScriptTypeAttributes: true,
//      removeStyleLinkTypeAttributes: true,
//      removeOptionalTags: true
//    })))
    // Output files
    .pipe($.if('*.html', $.size({title: 'html', showFiles: true})))
    .pipe(gulp.dest('unusualbusiness/templates'));
});


// Build SVG Sprites
let config              = {
    shape: {
        spacing: {
            padding: 5
        }
    },
    mode                : {
        // view            : {         // Activate the «view» mode
        //     bust        : false,
        //     render      : {
        //         scss    : true      // Activate Sass output (with default options)
        //     }
        // },
        // symbol          : true,      // Activate the «symbol» mode
        css: {
            dest: "./",
            layout: "diagonal",
            sprite: 'sprite',
            bust: false,
            render: {
                scss: {
                    dest: "../../assets/styles/base/_sprite.scss",
                    template: "unusualbusiness/assets/templates/sprite-template.scss"
                }
            }
        },
        variables: {
            mapname: "icons"
        }
    }
};

//https://www.liquidlight.co.uk/blog/article/creating-svg-sprites-using-gulp-and-sass/
gulp.task('svgSprite', () => {
    return gulp.src('**/*.svg', {cwd: 'unusualbusiness/assets/images'})
        .pipe(svgSprite(config))
        .pipe(gulp.dest('unusualbusiness/static/images'));
});

gulp.task('pngSprite', ['svgSprite'], function() {
	return gulp.src('unusualbusiness/static/images/sprite.svg')
		.pipe($.svg2png())
		.pipe($.size({
			showFiles: true
		}))
		.pipe(gulp.dest('unusualbusiness/static/images'));
});

gulp.task('svgStore', function () {
    var svgs = gulp
        .src('unusualbusiness/assets/images/*.svg')
        .pipe($.svgstore({ inlineSvg: true }));

    function fileContents (filePath, file) {
        return file.contents.toString();
    }

    return gulp
        .src('unusualbusiness/templates/blocks/svg_include.html')
        .pipe($.inject(svgs, { transform: fileContents }))
        .pipe(gulp.dest('unusualbusiness/templates/blocks'));
});

gulp.task('sprite', ['pngSprite', 'svgStore']);

// Clean output directory
gulp.task('clean', () => del(['.tmp'], {dot: true}));

// Build Production Files
gulp.task('build', ['clean'], function (cb) {
  // runSequence('styles', ['lint', 'scripts', 'html', 'fonts', 'sprite', 'images'], cb);
  runSequence('styles', ['lint', 'webpack', 'html', 'fonts', 'sprite', 'images'], cb);
});

// Watch Files For Changes & Reload, the default task
gulp.task('default', ['sprite', 'styles', 'webpack', 'images'], function () {
// gulp.task('default', ['sprite', 'styles', 'scripts', 'images'], function () {
  browserSync({
    notify: false,
    proxy: "127.0.0.1:8000"
    // proxy: "192.168.99.109:8000"
  });

  gulp.watch(['unusualbusiness/**/*.html'], reload);
  // gulp.watch(['unusualbusiness/assets/images/**/*'], ['images', 'sprite', reload]);
  gulp.watch(['unusualbusiness/assets/styles/**/*.{scss,css}'], ['styles', reload]);
  // gulp.watch(['unusualbusiness/assets/scripts/**/*.js'], ['scripts', reload]);
  gulp.watch(['unusualbusiness/assets/scripts/**/*.js'], ['webpack', reload]);
  gulp.watch('bower.json', ['fonts']);
});
