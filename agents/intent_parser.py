from models.intent import VideoIntent
from state import PipelineState
from utils.llm import llm


def intent_parser(state: PipelineState):

    prompt = state["prompt"]

    structured_model = llm.with_structured_output(VideoIntent)

    intent = structured_model.invoke(

        f"""

You are an AI Video Planner.

Convert the user's prompt into structured data.

Prompt:

{prompt}

Return

- pacing

- visual_style

- caption_tone

- transition_style

"""

    )

    return {

        "intent": intent

    }