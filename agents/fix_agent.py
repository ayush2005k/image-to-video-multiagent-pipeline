from state import PipelineState

from services.fix_service import fix_script


def fix_agent(state: PipelineState):

    print()

    print("========== FIX AGENT ==========")

    print()

    fixed_script = fix_script(

        script=state["remotion_script"],

        error=state["compile_error"]

    )

    print("✓ Script fixed")
    print()
    print(

    f"Retry Count : {state['retry_count'] + 1}"
    )

    print()

    return {

        "remotion_script": fixed_script,

        "retry_count": state["retry_count"] + 1

    }