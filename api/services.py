from main.services import rotate_image_handler
from main.models import Photo


def action_handler(photo, action):
    """ This function add rotation of uploaded photo or ignore it action is not define """

    if action == 'rotate_plus_90':
        rotate_image_handler(photo, angle=90)
    elif action == 'rotate_minus_90':
        rotate_image_handler(photo, angle=-90)
