from models.remotion import RemotionScript

from utils.llm import llm


def fix_script(

    script: RemotionScript,

    error: str

):

    prompt = f"""

You are a senior React and TypeScript engineer.

The following Remotion component failed to compile.

Fix the code.

Return ONLY the corrected code.

-------------------------

COMPILER ERROR

{error}

-------------------------

CURRENT CODE

{script.code}

"""

    response = llm.invoke(

        prompt

    )

    script.code = response.content

    return script