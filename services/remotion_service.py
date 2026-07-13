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

    prompt = f"""
{REMOTION_PROMPT}

--------------------------------------------------

REMOTION DOCUMENTATION

{remotion_docs}

--------------------------------------------------

STORYBOARD

{storyboard}

--------------------------------------------------

Generate a complete React TypeScript Remotion component.

IMPORTANT RULES:

1. Import everything like this:

import React from "react";

import {{
    AbsoluteFill,
    Sequence,
    Img,
    staticFile
}} from "remotion";

2. ALL images are stored in the public folder.

3. ALWAYS render images like this:

<Img
    src={{staticFile(scene.image)}}
    style={{
        width: "100%",
        height: "100%",
        objectFit: "cover"
    }}
/>

4. NEVER generate code like:

<Img src="goal1.jpg" />

5. Use ALL scenes from the storyboard.

6. Create exactly ONE Sequence for each storyboard scene.

7. Preserve:

- captions
- transitions
- timing
- duration

8. Return ONLY valid TypeScript code.

The filename must be:

GeneratedVideo.tsx
"""

    script = structured_llm.invoke(prompt)

    # Backup fix if the LLM forgets staticFile()

    script.code = script.code.replace(
        '<Img src="',
        '<Img src={staticFile("'
    )

    script.code = script.code.replace(
        '.jpg"',
        '.jpg")}'
    )

    script.code = script.code.replace(
        '.png"',
        '.png")}'
    )

    script.code = script.code.replace(
        '.jpeg"',
        '.jpeg")}'
    )

    # Add import if missing

    if "staticFile" not in script.code:

        script.code = script.code.replace(

            'Img,',

            '''Img,
    staticFile,'''
        )

    script = save_remotion_script(script)

    return script