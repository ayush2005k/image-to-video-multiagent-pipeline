from pathlib import Path

OUTPUT_DIR = Path("generated")

OUTPUT_DIR.mkdir(
    exist_ok=True
)


def save_remotion_script(script):

    path = OUTPUT_DIR / script.filename

    path.write_text(

        script.code,

        encoding="utf-8"

    )

    return path