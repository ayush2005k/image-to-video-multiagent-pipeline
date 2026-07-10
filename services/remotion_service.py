from models.remotion import RemotionScript

from prompts.remotion_prompt import REMOTION_PROMPT

from rag.retriever import retrieve_context

from utils.llm import llm

from utils.file_writer import save_remotion_script

def generate_remotion_script(storyboard):

    docs = retrieve_context(

        "Remotion React video component",

        k=1

    )

    remotion_docs = docs[0]["text"]

    structured_llm = llm.with_structured_output(

        RemotionScript

    )

    script = structured_llm.invoke(

        f"""
{REMOTION_PROMPT}

-----------------------

REMOTION DOCUMENTATION

{remotion_docs}

-----------------------

STORYBOARD

{storyboard}

Generate a React TypeScript Remotion component.

The filename should be:

GeneratedVideo.tsx
"""
    )

    save_remotion_script(script)

    return script