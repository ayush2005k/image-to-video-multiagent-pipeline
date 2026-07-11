from state import PipelineState

MAX_RETRIES = 1


def compiler_router(state: PipelineState):

    if state["compile_success"]:

        return "success"

    if state["retry_count"] >= MAX_RETRIES:

        print()
        print("Maximum retries reached.")
        print()

        return "success"

    return "retry"