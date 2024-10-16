from cms.extensions.toolbar import ExtensionToolbar
from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

class Post(models.Model):
    pass


class PostContentExtension(PageExtension):
    post_content = models.TextField()

extension_pool.register(PostContentExtension)


from cms.toolbar_pool import toolbar_pool


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



class MyTextPluginModel(CMSPlugin):
    text = models.CharField(max_length=255, verbose_name="Text")

    def __str__(self):
        return self.text

@plugin_pool.register_plugin  # Register the plugin
class MyTextPlugin(CMSPluginBase):
    model = MyTextPluginModel
    name = "Text Plugin"
    render_template = "my_text_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

