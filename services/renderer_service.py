import subprocess
from pathlib import Path


OUTPUT_DIR = Path("output")

OUTPUT_DIR.mkdir(
    exist_ok=True
)


def render_video():

    output_path = OUTPUT_DIR / "final_video.mp4"

    command = (
        "npx remotion render "
        "remotion/index.ts "
        "GeneratedVideo "
        f"{output_path}"
    )

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )
    print(result.returncode)

    return {

        "video_path": str(output_path),

        "success": result.returncode == 0,

        "logs": (result.stdout or "") + (result.stderr or "")
    }