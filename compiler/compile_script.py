import subprocess


def compile_remotion(script_path: str):

    try:

        command = "npx tsc --noEmit"

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=True
        )

        success = result.returncode == 0

        error = result.stderr + result.stdout

        return {
            "compile_success": success,
            "compile_error": error
        }

    except Exception as e:

        return {
            "compile_success": False,
            "compile_error": str(e)
        }