from state import PipelineState


def compiler_router(state: PipelineState):

    if state["compile_success"]:

        return "success"

    return "retry"