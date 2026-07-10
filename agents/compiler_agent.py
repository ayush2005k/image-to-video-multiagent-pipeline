from state import PipelineState

from compiler.compile_script import compile_remotion


def compiler_agent(state: PipelineState):

    print()

    print("========== COMPILER ==========")

    print()

    result = compile_remotion(

        state["remotion_script"].path

    )

    if result["compile_success"]:

        print("✓ Compilation successful")

    else:

        print("✗ Compilation failed")

        print()

        print(result["compile_error"][:1000])

    print()

    return {

        "compile_success": result["compile_success"],

        "compile_error": result["compile_error"]

    }