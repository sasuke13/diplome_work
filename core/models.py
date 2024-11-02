from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool


class PostContentExtension(PageExtension):
    post_content = models.TextField()


extension_pool.register(PostContentExtension)
