from models.intent import VideoIntent
from state import PipelineState
from utils.llm import llm


def intent_parser(state: PipelineState):

    prompt = state["prompt"]

    structured_model = llm.with_structured_output(VideoIntent)

    intent = structured_model.invoke(

        f"""

You are an AI Video Planner.

Extract the following fields.

Rules:

1. pacing:
Choose exactly one:
slow
medium
fast

2. visual_style:
Choose exactly one:
cinematic
upbeat
corporate
modern
luxury
documentary

3. caption_tone:
Choose exactly one:
minimal
bold
emotional
professional

4. transition_style:
Choose exactly one:
fade
cut
zoom
crossfade
slide

Only choose from these options.

User Prompt:


{prompt}

Return

- pacing

- visual_style

- caption_tone

- transition_style

"""

    )

   