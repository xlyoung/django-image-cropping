"""
Backend for "easy_thumbnails" package. This module can't be named
"easy_thumbnails" in order to avoid Python import conflicts.
"""

from .base import ImageBackend

from easy_thumbnails.files import get_thumbnailer
from easy_thumbnails.source_generators import pil_image
from easy_thumbnails.exceptions import InvalidImageFormatError


class EasyThumbnailsBackend(ImageBackend):
    exceptions_to_catch = (InvalidImageFormatError, IOError)

    def get_thumbnail_url(self, image_path, thumbnail_options):
        thumb = get_thumbnailer(image_path)
        return thumb.get_thumbnail(thumbnail_options).url

    def get_size(self, image):
        return pil_image(image).size
