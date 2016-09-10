# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import unusualbusiness.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_nl', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_nl', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_en', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_nl', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_nl', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_nl', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='OrganizationPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_nl', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_nl', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_en', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_nl', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_nl', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_nl', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('format', models.CharField(choices=[(b'organization', 'Practitioner')], default='organization', max_length=32, verbose_name='page_format')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Is Featured on home page')),
                ('description', models.TextField(blank=True, max_length=1024, verbose_name='Description')),
                ('description_nl', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, max_length=1024, null=True, verbose_name='Description')),
                ('date_founded', models.DateField(blank=True, null=True, verbose_name='Founded date')),
                ('amount_of_members', models.PositiveIntegerField(blank=True, null=True, verbose_name='Amount of members')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='Address')),
                ('postal_code', models.CharField(blank=True, max_length=8, verbose_name='Postal code')),
                ('city', models.CharField(blank=True, max_length=64, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=64, verbose_name='Country')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('website', models.URLField(blank=True, verbose_name='Website')),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, verbose_name='Twitter')),
                ('featured_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Featured image')),
            ],
            options={
                'verbose_name': 'Practitioner',
                'verbose_name_plural': 'Practitioners',
            },
            bases=('wagtailcore.page', unusualbusiness.utils.models.RenderInlineMixin, unusualbusiness.utils.models.RelatedHowToMixin),
        ),
    ]
