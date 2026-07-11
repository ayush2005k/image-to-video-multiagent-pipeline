from state import PipelineState

from utils.image_loader import load_images
from services.vision_service import analyze_image


def image_analyzer(state: PipelineState):

    images = load_images("./public")

    analyses = []

    print("\n========== Image Analyzer ==========\n")

    for image in images:

        print(f"Analyzing {image.name}...")

        try:

            result = analyze_image(image)

            analyses.append(result)

            print("✓ Done")

        except Exception as e:

            print(f"✗ Failed : {e}")

    print("\n====================================\n")

    return {

        "image_analysis": analyses

    }