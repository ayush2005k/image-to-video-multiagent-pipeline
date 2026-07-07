from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()


def open_image(image_path):
    return Image.open(image_path)


def get_image_size(image_path):

    with Image.open(image_path) as img:
        return img.size