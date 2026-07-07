from pathlib import Path


SUPPORTED_FORMATS = [".jpg", ".jpeg", ".png"]


def load_images(folder):

    folder = Path(folder)

    images = []

    for file in folder.iterdir():

        if file.suffix.lower() in SUPPORTED_FORMATS:

            images.append(file)

    return sorted(images)