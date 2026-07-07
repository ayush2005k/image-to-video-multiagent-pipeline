from pathlib import Path

SUPPORTED_FORMATS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".heic",
    ".heif"
}


def load_images(folder: str):

    folder = Path(folder)

    if not folder.exists():
        raise FileNotFoundError(f"{folder} does not exist.")

    images = []

    for image in folder.iterdir():

        if image.suffix.lower() in SUPPORTED_FORMATS:

            images.append(image)

    return sorted(images)