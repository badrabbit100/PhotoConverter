import os
from django.core.exceptions import ValidationError
from PIL import Image
from OnlineConverter import settings
from .models import Photo


def validate_photo_extension(value):
    """
        Validate Photo format and file size before save in Server
        Limit = 5Mb
        Receive Formats .jpg, .png, .jpeg Only
    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg']
    valid_size = 5242880
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file type')
    if value.size > valid_size:
        raise ValidationError('Unsupported file size. Max-size is 5 Mb')


def rotate_image(path, angle):
    """ This function modify income image and save it in storage """

    image = Image.open(path)
    rotated_image = image.rotate(angle, expand=True)
    rotated_image.save(path)


def rotate_image_handler(photos, angle):
    """ Function check is objects iterable or not, than modify image by rotate_image func, RETURN NONE  """

    current_folder = os.getcwd()
    if hasattr(photos, '__iter__'):
        for photo in photos:
            rotate_image(path=current_folder + photo.photo_input.url, angle=angle)
    else:
        rotate_image(path=current_folder + photos.photo_input.url, angle=angle)
