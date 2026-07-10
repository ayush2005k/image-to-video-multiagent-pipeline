from compiler.compile_script import compile_remotion


result = compile_remotion(

    "generated/GeneratedVideo.tsx"

)

print()

print(result["compile_success"])

print()

print(result["compile_error"])

print()