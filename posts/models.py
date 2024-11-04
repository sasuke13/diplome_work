import os

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from django.db import models
from cms.extensions import PageExtension

from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class PostContentExtension(PageExtension):
    post_content = models.TextField()


class MyTextPluginModel(CMSPlugin):
    text = models.CharField(max_length=255, verbose_name="Text")

    def __str__(self):
        return self.text


class CooperationPluginModel(CMSPlugin):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    image1 = models.ImageField(
        verbose_name=_("Image 1"),
        upload_to='uploads/'
    )
    image2 = models.ImageField(
        verbose_name=_("Image 2"),
        upload_to='uploads/'
    )

    def __str__(self):
        return self.title

    def get_image1_url(self):
        if self.image1:
            return os.path.join(static('media'), os.path.basename(self.image1.name))
        return None

    def get_image2_url(self):
        if self.image2:
            return static(f'{self.image2.name}')
        return None


class TextSectionPluginModel(CMSPlugin):
    title = models.CharField(_("Title"), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title or "Text Section"


class Paragraph(models.Model):
    text_section = models.ForeignKey(
        TextSectionPluginModel,
        related_name="paragraphs",
        on_delete=models.CASCADE
    )
    content = models.TextField(_("Content"))

    def __str__(self):
        return self.content[:50]


class ProjectSectionPluginModel(CMSPlugin):
    title = models.CharField(_("Title"), max_length=255, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    image = FilerImageField(
        verbose_name=_("Image"),
        on_delete=models.CASCADE,
        related_name="project_section_image"
    )

    def __str__(self):
        return self.title or "Project Section"


class PicturePluginModel(CMSPlugin):
    image = FilerImageField(
        verbose_name=_("Image"),
        on_delete=models.CASCADE,
        related_name="picture"
    )


class Review(models.Model):
    full_name = models.CharField(max_length=255)
    review_text = models.TextField()
    date = models.DateField()
    photo = models.ImageField(upload_to='reviews/')

    def __str__(self):
        return f"{self.full_name} - {self.date}"


class ReviewPlugin(CMSPlugin):
    reviews = models.ManyToManyField(Review, related_name='review_plugins')


class ReviewPluginModel(CMSPluginBase):
    model = ReviewPlugin
    name = "Review Carousel"
    render_template = "plugins/feedbacks.html"
    cache = False


class ImageCarousel(CMSPlugin):
    title = models.CharField(max_length=255, verbose_name=_("Main Title"))


class CarouselSlide(CMSPlugin):
    photo = models.ImageField(upload_to='carousel_slides/')


class TextBesideTheImage(CMSPlugin):
    text = models.TextField()
    image = models.ImageField(upload_to='pictures/')


from cms.extensions.toolbar import ExtensionToolbar
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from cms.extensions.extension_pool import extension_pool
from cms.toolbar_pool import toolbar_pool

extension_pool.register(PostContentExtension)


@toolbar_pool.register
class IconExtensionToolbar(ExtensionToolbar):
    model = PostContentExtension

    def populate(self):
        current_page_menu = self._setup_extension_toolbar()
        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()
            if url:
                current_page_menu.add_modal_item('Post Content', url=url,
                                                 disabled=not self.toolbar.edit_mode)


@plugin_pool.register_plugin
class MyTextPlugin(CMSPluginBase):
    model = MyTextPluginModel
    name = "Text Plugin"
    render_template = "plugins/my_text_plugin.html"
    module = _("University Components")

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


@plugin_pool.register_plugin
class CooperationPlugin(CMSPluginBase):
    model = CooperationPluginModel
    render_template = "plugins/text_between_2_pictures.html"
    cache = False
    name = _("Text between 2 images")
    module = _("University Components")
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class ProjectSectionPlugin(CMSPluginBase):
    model = ProjectSectionPluginModel
    render_template = "plugins/text_with_picture.html"
    name = _("Project Section")
    module = _("University Components")
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class PicturePlugin(CMSPluginBase):
    model = PicturePluginModel
    render_template = "plugins/picture.html"
    name = _("Picture Section")
    module = _("University Components")
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


plugin_pool.register_plugin(ReviewPluginModel)


@plugin_pool.register_plugin
class ImageCarouselSlidePlugin(CMSPluginBase):
    model = CarouselSlide
    name = _("Carousel Slide")
    render_template = "plugins/carousel_slide.html"
    module = _("University Components")
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class ImageCarouselPlugin(CMSPluginBase):
    model = ImageCarousel
    name = _("Image Carousel")
    render_template = "plugins/photo_carousel.html"
    module = _("University Components")
    allow_children = True
    child_classes = ["ImageCarouselSlidePlugin"]
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class TextBesideThePicture(CMSPluginBase):
    model = TextBesideTheImage
    name = _("Text Beside The Picture")
    render_template = "plugins/text_picture.html"
    module = _("Text And Picture Section")
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class PictureBesideTheText(CMSPluginBase):
    model = TextBesideTheImage
    name = _("Picture Beside The Text")
    render_template = "plugins/picture_text.html"
    module = _("Text And Picture Section")
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


@plugin_pool.register_plugin
class TextAndPictureSection(CMSPluginBase):
    name = _("Text And Picture Section")
    render_template = "plugins/content_section.html"
    module = _("Text And Picture Section")
    allow_children = True
    child_classes = ["TextBesideThePicture", "PictureBesideTheText"]
    cache = False

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
