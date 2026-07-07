VISION_PROMPT = """
Analyze this event image.

Return ONLY valid JSON.

No markdown.

No explanation.

Schema

{
"description":"",
"emotion":"",
"scene_type":"",
"people_count":0,
"importance":1
}

importance:

1 = not useful

10 = must include

description should be one sentence.

emotion should be one word.

scene_type examples

portrait

group

food

dance

stage

selfie

ceremony

landscape

travel
"""