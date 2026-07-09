from models.storyboard import Storyboard


def validate_storyboard(storyboard: Storyboard):

    if len(storyboard.scenes) == 0:
        raise ValueError(
            "Storyboard contains no scenes."
        )

    total_duration = 0

    previous_start = 0

    for scene in storyboard.scenes:

        if scene.duration <= 0:

            raise ValueError(

                f"{scene.image} has invalid duration."

            )

        if scene.start_time < previous_start:

            raise ValueError(

                "Scenes are not in chronological order."

            )

        previous_start = scene.start_time

        total_duration += scene.duration

    storyboard.total_duration = total_duration

    return storyboard