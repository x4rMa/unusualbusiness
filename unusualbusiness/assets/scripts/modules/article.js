/* ==|====================
   Module/Article
   ======================= */

'use strict';

import gumshoe from 'gumshoe';
import Clipboard from 'clipboard';
import tocbot from 'tocbot';
import Fraccordion from '../vendor/accordion';

let Article = () => {
  let initInlineArticleLinks = function() {
    let articleInlineLinks = $('.article-inline-link');

    articleInlineLinks.on('click', function() {
      let inlineElement = $(this).data('id');

      $(this).toggleClass('is-expanded');
      $('#' + inlineElement).each( function () {
        $(this).toggleClass('is-visuallyhidden animated fadeIn');
      });
    });
  };

  let initStickyTOC = function() {
    if($.fn.sticky !== undefined) {
      $(".toc-wrapper ").sticky({
        topSpacing: 100,
        bottomSpacing: 2500
      });
    } else {
      console.error('jQuery sticky not defined');
    }
  };

  let initTOC = function() {
    initTOCSlideIn();
    addIdsToHeadings();
    initGumshoe();
    initStickyTOC();

    tocbot.init({
      // Where to render the table of contents.
      tocSelector: '#toc',
      // Where to grab the headings to build the table of contents.
      contentSelector: '.l-boxed',
      // Which headings to grab inside of the contentSelector element.
      headingSelector: 'h1, h2, h3',
      listClass:  'toc-list',
      extraListClasses: 'animated fadeInLeft',
      linkClass: 'toc-link'
    });
  };

  let initTOCSlideIn = function() {
    let $tocWrapper = $('.toc-wrapper');
    let $tocToggleLink = $('.toggle-toc-link');
    let $toc = $('.article-table-of-contents');
    let $articleIntroduction = $('.article-introduction');
    let $blockImage = $('.block-image');

    $tocToggleLink.on('click', function() {
      $tocToggleLink.toggleClass('is-panel-open');
      $toc.toggleClass('is-closed');
      $articleIntroduction.toggleClass('l-pull-right');
      $blockImage.toggleClass('l-pull-right');

      return false;
    });
  };

  let initFraccordion = function () {
    var myAccordion = Fraccordion({
      // String - Outer container selector, hook for JS init() method
      selector: '.js-fr-accordion',

      // String - Accordion header elements converted to focusable, togglable elements
      headerSelector: '.js-fr-accordion__header',

      // String - Use header id on element to tie each accordion panel to its header - see panelIdPrefix
      headerIdPrefix: 'accordion-header',

      // String - Accordion panel elements to expand/collapse
      panelSelector: '.js-fr-accordion__panel',

      // String - Use panel id on element to tie each accordion header to its panel - see headerIdPrefix
      panelIdPrefix: 'accordion-panel',

      // Boolean - If set to false, all accordion panels will be closed on init()
      firstPanelsOpenByDefault: false,

      // Boolean - If set to false, each accordion instance will only allow a single panel to be open at a time
      multiselectable: false,

      // String - Class name that will be added to the selector when the component has been initialised
      readyClass: 'fr-accordion--is-ready',

      // Integer - Duration (in milliseconds) of CSS transition when opening/closing accordion panels
      transitionLength: 250
    });

  };

  let initArticleNotes = function() {
    let articleFootnotes = $('.article-inline-footnote');

    articleFootnotes.each(function() {
      let footnoteIndex = $(this).attr('id').split('-')[2];
      let articleFootnoteLink = $('#article-footnote-link-' + footnoteIndex);
      articleFootnoteLink.after($(this).detach());
    });
  };
  let initSocialLinks = function() {
    let $moreSocialLink = $('.more-social-link');
    let $socialListItem = $('.social-list-item');


    $moreSocialLink.on('click', function() {
      $socialListItem.removeClass('is-hidden');
      return false;
    });
  };

  let initSocialLinksModal = function() {
    let $articleHeader = $('.article-header');
    let $articleSubheader = $('.article-subheader');
    let $openSocialModal = $('.open-social-modal');
    let $openAuthorPaneButton = $('.open-author-pane-button');

    $openSocialModal.on('click', function() {
      let status = $(this).attr('data-closed');
      console.log(status);
      if( status === 'true' ) { // Opening
        console.log('Opening');

        $openSocialModal.parent().toggleClass('is-open-social');

        $articleHeader.toggleClass('is-no-position');
        if( $articleSubheader.hasClass('slideOutDown')) {
          $articleSubheader.removeClass('slideOutDown');
        }

        $articleSubheader.addClass('animated slideInUp is-show-article-subheader');
        $openAuthorPaneButton.toggleClass('is-hidden');
        $(this).attr('data-closed', 'false');

      } else { // Closing
        console.log('Closing');

        $openSocialModal.parent().toggleClass('is-open-social');

        $articleSubheader.removeClass('slideInUp');
        $articleSubheader.addClass('slideOutDown ');
        $articleSubheader.removeClass('is-show-article-subheader');
        $openAuthorPaneButton.toggleClass('is-hidden');
        $articleHeader.toggleClass('is-no-position');
        $(this).attr('data-closed', 'true');
      }
    });
  };

  let addIdsToHeadings = function() {
    let $headings = $('.l-boxed h2,.l-boxed h3,.l-boxed h4');

    $headings.each( function() {
      let text = this.innerText;
      let slug = slugify(text);
      $(this).attr('id', slug);
    })
  };

  let slugify = function(text) {
    return text.toString().toLowerCase()
      .replace(/\s+/g, '-')           // Replace spaces with -
      .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
      .replace(/\-\-+/g, '-')         // Replace multiple - with single -
      .replace(/^-+/, '')             // Trim - from start of text
      .replace(/-+$/, '');            // Trim - from end of text
  };

  let initCopyUrlToClipboard = function() {
    new Clipboard('.copy-url-link');
  };

  let initGumshoe = function() {
    gumshoe.init();
  };

  let init = function() {
    console.log('Article go!');

    initArticleNotes();
    initInlineArticleLinks();

    // Only with theory article
    if( $('body').hasClass('theory-article')) {
      initTOC();
    }

    initFraccordion();
    initSocialLinks();
    initSocialLinksModal();
    initCopyUrlToClipboard();
  };

  return {
    init: init
  };
};

export default Article;
