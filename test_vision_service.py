from pathlib import Path

from services.vision_service import analyze_image

image = Path("assets/IMG_0704.jpg")

result = analyze_image(image)

print()

print(result)

print()