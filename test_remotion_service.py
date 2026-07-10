from services.remotion_service import generate_remotion_script

from models.storyboard import Storyboard
from models.storyboard import StoryboardScene


storyboard = Storyboard(

    title="Demo",

    total_duration=4,

    scenes=[

        StoryboardScene(

            image="IMG_0704.jpg",

            start_time=0,

            duration=4,

            caption="Beautiful memory",

            transition="fade",

            reason="Opening scene"

        )

    ]

)

script = generate_remotion_script(

    storyboard

)

print()

print(script.filename)

print()

print(script.code[:1000])

print()