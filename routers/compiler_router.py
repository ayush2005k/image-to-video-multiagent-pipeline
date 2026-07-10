from state import PipelineState


MAX_RETRIES = 3


def compiler_router(state: PipelineState):

    if state["compile_success"]:

        return "success"

    if state["retry_count"] >= MAX_RETRIES:

        return "success"

    return "retry"