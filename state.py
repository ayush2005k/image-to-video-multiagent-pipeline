from typing import TypedDict

from models.intent import VideoIntent
from models.image import ImageAnalysis
from models.storyboard import StoryboardScene
from models.storyboard import Storyboard

class PipelineState(TypedDict):

    prompt:str

    intent:VideoIntent

    image_analysis:list[ImageAnalysis]

    selected_images:list[str]

    storyboard: Storyboard

    remotion_script:str

    compile_success:bool

    compile_error:str

    retry_count:int

    final_video:str