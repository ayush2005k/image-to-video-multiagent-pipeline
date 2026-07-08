from graph.pipeline import graph

initial_state = {

    "prompt": "Cinematic wedding reel, slow and emotional, warm tones, minimal text",

    "retry_count": 0

}

result = graph.invoke(initial_state)

print()

print("========== VIDEO INTENT ==========")

print(result["intent"])

print()

print("========== IMAGE ANALYSIS ==========\n")

for image in result["image_analysis"]:

    print(image)

    print()

print("=" * 50)