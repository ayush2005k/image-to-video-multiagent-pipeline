VISION_PROMPT = """
You are an expert event photographer.

Analyze this image.

Return ONLY JSON.

Schema:

{
  "description": "",
  "emotion": "",
  "scene_type": "",
  "people_count": 0,
  "importance": 1
}

Rules

importance:
1 = irrelevant
10 = must include

people_count = integer

No markdown.
No explanation.
"""