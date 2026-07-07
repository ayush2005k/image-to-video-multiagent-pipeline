from utils.image_loader import load_images
from utils.image_utils import get_image_size

images = load_images("./assets")

for image in images:

    width, height = get_image_size(image)

    print()

    print(image.name)

    print(width, height)