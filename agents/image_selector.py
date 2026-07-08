from state import PipelineState


def image_selector(state: PipelineState):

    analyses = state["image_analysis"]

    selected = []

    print("\n========== Image Selector ==========\n")

    for image in analyses:

        if image.importance >= 7:

            selected.append(image.filename)

            print(f"✓ Selected : {image.filename}")

        else:

            print(f"✗ Skipped : {image.filename}")

    print("\n===================================\n")

    return {

        "selected_images": selected

    }