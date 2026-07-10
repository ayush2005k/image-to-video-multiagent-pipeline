from graph.pipeline import graph

initial_state = {

    "prompt": "Cinematic wedding reel, slow and emotional, warm tones, minimal text",

    "retry_count": 0

}

result = graph.invoke(initial_state)

# =====================================================
# VIDEO INTENT
# =====================================================

print()

print("=" * 60)
print("VIDEO INTENT")
print("=" * 60)

print(result["intent"])

# =====================================================
# IMAGE ANALYSIS
# =====================================================

print()

print("=" * 60)
print("IMAGE ANALYSIS")
print("=" * 60)

for image in result["image_analysis"]:

    print(image)
    print()

# =====================================================
# SELECTED IMAGES
# =====================================================

print()

print("=" * 60)
print("SELECTED IMAGES")
print("=" * 60)

for image in result["selected_images"]:

    print(image)

# =====================================================
# STORYBOARD
# =====================================================

print()

print("=" * 60)
print("STORYBOARD")
print("=" * 60)

storyboard = result["storyboard"]

print(f"Title          : {storyboard.title}")
print(f"Total Duration : {storyboard.total_duration} sec")

print()

print("Scenes")

print("-" * 60)

for i, scene in enumerate(storyboard.scenes, start=1):

    print(f"Scene {i}")

    print(f"Image       : {scene.image}")
    print(f"Start Time  : {scene.start_time}")
    print(f"Duration    : {scene.duration}")
    print(f"Caption     : {scene.caption}")
    print(f"Transition  : {scene.transition}")
    print(f"Reason      : {scene.reason}")

    print("-" * 60)

print()
print()

print("=" * 60)
print("REMOTION SCRIPT")
print("=" * 60)

script = result["remotion_script"]

print(f"Filename : {script.filename}")

print()

print(script.code[:1000])

print()