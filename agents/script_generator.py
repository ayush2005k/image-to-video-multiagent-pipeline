from state import PipelineState

from services.remotion_service import generate_remotion_script


def script_generator(state: PipelineState):

    print()

    print("========== SCRIPT GENERATOR ==========")

    print()

    script = generate_remotion_script(

        storyboard=state["storyboard"]

    )

    print(f"✓ Script generated")

    print(f"File : {script.filename}")

    print()

    return {

        "remotion_script": script

    }