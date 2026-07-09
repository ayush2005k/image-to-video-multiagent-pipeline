from state import PipelineState

from services.storyboard_service import generate_storyboard


def storyboard_writer(state: PipelineState):

    print("\n========== STORYBOARD WRITER ==========\n")

    storyboard = generate_storyboard(

        intent=state["intent"],

        selected_images=state["selected_images"],

        image_analysis=state["image_analysis"]

    )

    print("✓ Storyboard Generated")

    print(
        f"Scenes : {len(storyboard.scenes)}"
    )
    print(
        f"Total Duration : {storyboard.total_duration} sec"
    )

    return {

        "storyboard": storyboard

    }