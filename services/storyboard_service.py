from models.storyboard import Storyboard

from prompts.storyboard_prompt import STORYBOARD_PROMPT

from rag.retriever import retrieve_context

from utils.llm import llm

from validators.storyboard_validator import validate_storyboard


def generate_storyboard(

        intent,

        selected_images,

        image_analysis

):

    style_docs = retrieve_context(

        intent.visual_style,

        k=1

    )

    style_guide = style_docs[0]["text"]

    structured_llm = llm.with_structured_output(

        Storyboard

    )

    storyboard = structured_llm.invoke(

        f"""
{STORYBOARD_PROMPT}

----------------------------

VIDEO INTENT

{intent}

----------------------------

STYLE GUIDE

{style_guide}

----------------------------

SELECTED IMAGES

{selected_images}

----------------------------

IMAGE ANALYSIS

{image_analysis}

"""
    )

    storyboard = validate_storyboard(storyboard)

    return storyboard