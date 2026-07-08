from state import PipelineState


def storyboard_writer(state: PipelineState):

    print("\n========== STORYBOARD WRITER ==========\n")

    print("Intent")

    print(state["intent"])

    print()

    print("Selected Images")

    print(state["selected_images"])

    print()

    print("Loading style guide...")

    print()

    return {}