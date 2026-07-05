from graph.pipeline import graph

initial_state = {

    "prompt":

    "Cinematic wedding reel, slow and emotional, warm tones, minimal text",

    "retry_count":0

}

result = graph.invoke(

    initial_state

)

print()

print(result["intent"])

print()