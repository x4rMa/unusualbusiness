from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase, CommonGenericTaggedItemBase, GenericUUIDTaggedItemBase, Tag
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail_modeltranslation.models import TranslationMixin

from unusualbusiness.events.models import EventPage
from unusualbusiness.tags.models import TheoryArticlePageTag, StoryArticlePageTag, ReportArticlePageTag


class TheoryArticleIndexPage(TranslationMixin, Page):

    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.TheoryArticlePage']

    def get_context(self, request):
        context = super(TheoryArticleIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['articles'] = TheoryArticlePage.objects.all().live()
        context['parent'] = self.get_parent()
        return context


class StoryArticleIndexPage(TranslationMixin, Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['articles.StoryArticlePage']

    def get_context(self, request):
        context = super(StoryArticleIndexPage, self).get_context(request)
        # Add extra variables and return the updated context
        context['articles'] = StoryArticlePage.objects.all().live()
        context['parent'] = self.get_parent()
        return context


class AbstractArticle(models.Model):

    subtitle = models.CharField(
        verbose_name=_('subtitle'),
        max_length=255,
        help_text=_("The subtitle of the page"),
        blank=True
    )
    author = models.CharField(
        verbose_name=_('author'),
        max_length=255,
        help_text=_("The author of the article")
    )
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('featured_image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    summary = models.TextField(
        verbose_name=_('summary'),
        help_text=_("The summary of the articles (max 100 words)"),
        blank=True
    )
    publication_date = models.DateField(
        verbose_name=_('publication_date'),
        help_text=_("The publication date of the article"),
        blank=True
    )
    body = RichTextField(
        verbose_name=_('body text'),
        help_text=_("The main text of the article"),
        blank=True
    )

    class Meta:
        abstract = True
        verbose_name = _("Article")


class StoryArticlePage(TranslationMixin, Page, AbstractArticle):
    parent_page_types = ['articles.StoryArticleIndexPage']
    subpage_types = []

    tags = ClusterTaggableManager(through=StoryArticlePageTag, blank=True)

    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

StoryArticlePage.content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('author'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        FieldPanel('body'),
        InlinePanel('organizations', label=_("Organizations")),
        FieldPanel('tags'),
    ]

StoryArticlePage.promote_panels = Page.promote_panels

StoryArticlePage.search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('subtitle_en'),
        index.SearchField('subtitle_nl'),
        index.SearchField('author'),
        index.SearchField('summary_en'),
        index.SearchField('summary_nl'),
        index.SearchField('body_en'),
        index.SearchField('body_nl'),
        index.RelatedFields('organizations', [
            index.SearchField('title'),
        ]),
        index.RelatedFields('how_to_page', [
            index.SearchField('title'),
        ]),
    )


class StoryArticlePageOrganization(Orderable, models.Model):
    story_article_page = ParentalKey('articles.StoryArticlePage', related_name='organizations')
    organization_page = models.ForeignKey(
        'organizations.OrganizationPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='story_article_page'
    )

    panels = [
          PageChooserPanel('organization_page'),
    ]

    def __str__(self):              # __unicode__ on Python 2
        return self.story_article_page.title + " -> " + self.organization_page.title


class TheoryArticlePage(TranslationMixin, Page, AbstractArticle):
    parent_page_types = ['articles.TheoryArticleIndexPage']
    subpage_types = []

    tags = ClusterTaggableManager(through=TheoryArticlePageTag, blank=True)

    class Meta:
        verbose_name = _("Theory")
        verbose_name_plural = _("Theories")

TheoryArticlePage.content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('author'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        FieldPanel('body'),
        FieldPanel('tags'),
    ]

TheoryArticlePage.promote_panels = Page.promote_panels

TheoryArticlePage.search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('subtitle_en'),
        index.SearchField('subtitle_nl'),
        index.SearchField('author'),
        index.SearchField('summary_en'),
        index.SearchField('summary_nl'),
        index.SearchField('body_en'),
        index.SearchField('body_nl'),
        index.RelatedFields('how_to_page', [
            index.SearchField('title'),
        ]),
    )


class ReportArticlePage(TranslationMixin, Page, AbstractArticle):
    event_page = models.ForeignKey(
        'events.EventPage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='report_article_page'
    )
    tags = ClusterTaggableManager(through=ReportArticlePageTag, blank=True)

    parent_page_types = ['events.EventPage']
    subpage_types = []

    class Meta:
        verbose_name = _("Event report")

ReportArticlePage.content_panels = Page.content_panels + [
        PageChooserPanel('event_page'),
        FieldPanel('subtitle'),
        FieldPanel('author'),
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('publication_date'),
        FieldPanel('body'),
        FieldPanel('tags'),
    ]

ReportArticlePage.promote_panels = Page.promote_panels

ReportArticlePage.search_fields = Page.search_fields + (
        index.SearchField('title_en'),
        index.SearchField('title_nl'),
        index.SearchField('subtitle_en'),
        index.SearchField('subtitle_nl'),
        index.SearchField('author'),
        index.SearchField('summary_en'),
        index.SearchField('summary_nl'),
        index.SearchField('body_en'),
        index.SearchField('body_nl'),
        index.RelatedFields('event_page', [
            index.SearchField('title'),
        ]),
    )
