from services.storyboard_service import generate_storyboard

from models.intent import VideoIntent

from models.image import ImageAnalysis


intent = VideoIntent(

    pacing="slow",

    visual_style="cinematic",

    caption_tone="minimal",

    transition_style="fade"

)


images = [

    "IMG_0704.jpg"

]


analysis = [

    ImageAnalysis(

        filename="IMG_0704.jpg",

        description="Smiling young man sitting in a cafe.",

        emotion="happy",

        scene_type="portrait",

        people_count=1,

        importance=8

    )

]


storyboard = generate_storyboard(

    intent,

    images,

    analysis

)

print()

print(storyboard)

print()