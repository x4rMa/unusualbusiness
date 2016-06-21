# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import unusualbusiness.utils.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_nl', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_en', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_nl', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_nl', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_nl', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_nl', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('format', models.CharField(choices=[(b'event', 'Activity')], default='event', max_length=32, verbose_name='page_format')),
                ('event_type', models.CharField(blank=True, max_length=512, verbose_name='Type of event')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Is Featured on home page')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Starting date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End date')),
                ('venue_name', models.CharField(blank=True, max_length=128, verbose_name='Venue')),
                ('venue_address', models.CharField(blank=True, max_length=128, verbose_name='Address')),
                ('venue_postal_code', models.CharField(blank=True, max_length=8, verbose_name='Postal code')),
                ('venue_city', models.CharField(blank=True, max_length=64, verbose_name='City')),
                ('venue_country', models.CharField(blank=True, max_length=64, verbose_name='Country')),
                ('description', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))]))])),
                ('description_en', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))]))], null=True)),
                ('description_nl', wagtail.wagtailcore.fields.StreamField([('introduction', wagtail.wagtailcore.blocks.TextBlock(icon='italic', rows=3)), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('pullquote', wagtail.wagtailcore.blocks.StructBlock([(b'pull_quote', wagtail.wagtailcore.blocks.TextBlock(required=True, rows=2, verbose_name='Pull quote')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(help_text='The name of the person or organization that the quote can be attributed to quote', required=False, verbose_name='Quote attribution to')), (b'link', wagtail.wagtailcore.blocks.URLBlock(help_text='Click quote to go to link.', required=False, verbose_name='Link'))]))], null=True)),
                ('facebook_event', models.URLField(blank=True, verbose_name='Facebook event')),
                ('featured_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Featured image')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=('wagtailcore.page', unusualbusiness.utils.models.RenderInlineMixin, unusualbusiness.utils.models.RelatedHowToMixin),
        ),
    ]
