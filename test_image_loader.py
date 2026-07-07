from utils.image_loader import load_images

images = load_images("./assets")

print()

print(f"Found {len(images)} images")

print()

for image in images:

    print(image.name)