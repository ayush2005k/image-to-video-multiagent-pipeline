from state import PipelineState

from services.renderer_service import render_video


def renderer_agent(state: PipelineState):

    print()

    print("========== RENDERER ==========")

    print()

    result = render_video()

    if result["success"]:

        print("✓ Video rendered")

        print()

        print(result["video_path"])

    else:

        print("✗ Rendering failed")

    return {

        "final_video": result["video_path"]

    }