import subprocess


def compile_remotion(script_path: str):

    try:

        result = subprocess.run(

            [

                "npx",

                "tsc",

                "--noEmit",

                script_path

            ],

            capture_output=True,

            text=True

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