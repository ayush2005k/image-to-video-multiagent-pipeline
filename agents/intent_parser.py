from models.intent import VideoIntent
from state import PipelineState
from utils.llm import llm


def intent_parser(state: PipelineState):

    prompt = state["prompt"]

    structured_model = llm.with_structured_output(VideoIntent)

    intent = structured_model.invoke(
        f"""
You are an AI Video Planner.

Analyze the user's prompt and populate the VideoIntent schema.

Rules:

- pacing: choose ONLY one of: slow, medium, fast
- visual_style: choose ONLY one of: cinematic, upbeat, corporate, modern, luxury, documentary
- caption_tone: choose ONLY one of: minimal, bold, emotional, professional
- transition_style: choose ONLY one of: fade, cut, zoom, crossfade, slide

Never invent new values.
Never combine multiple values.
Select the closest matching option from the allowed list.

User Prompt:

{prompt}
"""
    )

    return {
        "intent": intent
    }