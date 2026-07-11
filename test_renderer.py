from services.renderer_service import render_video


result = render_video()

print()

print(result["success"])

print()

print(result["video_path"])

print()

print(result["logs"])