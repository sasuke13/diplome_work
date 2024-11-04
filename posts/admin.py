from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from posts.models import Paragraph, TextSectionPluginModel, ReviewPlugin, Review


# Carousel


# Carousel


# Feedbacks

class ReviewInline(admin.TabularInline):
    model = ReviewPlugin.reviews.through
    extra = 1


@admin.register(ReviewPlugin)
class ReviewPluginAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date')
    search_fields = ('full_name', 'review_text')

# Feedbacks


class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 1
    verbose_name = "Paragraph"
    verbose_name_plural = "Paragraphs"


@plugin_pool.register_plugin
class TextSectionPlugin(CMSPluginBase):
    model = TextSectionPluginModel
    render_template = "plugins/text_section_plugin.html"
    name = _("Text Section")
    module = _("University Components")
    cache = False
    inlines = [ParagraphInline]
    allow_children = True
    child_classes = ["TextPlugin", "PicturePlugin", "LinkPlugin", "TextAndPictureSection"]

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['paragraphs'] = instance.paragraphs.all()
        return context
