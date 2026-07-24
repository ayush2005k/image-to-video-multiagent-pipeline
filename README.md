# Image-to-Video Multi-Agent Pipeline

An AI-powered multi-agent system that converts a collection of images into an engaging video automatically using Large Language Models, LangGraph, computer vision, and Remotion.

## Features

- Multi-agent workflow using LangGraph
- Image understanding using Vision AI
- Intelligent image selection
- AI-generated storyboard
- Automatic Remotion TypeScript code generation
- TypeScript compilation and validation
- Automatic code fixing with retry mechanism
- Video rendering using Remotion
- Retrieval-Augmented Generation (RAG) for Remotion documentation
- End-to-end automated pipeline

## Architecture

```
User Prompt
      │
      ▼
Intent Parser
      │
      ▼
Image Analyzer
      │
      ▼
Image Selector
      │
      ▼
Storyboard Writer
      │
      ▼
Script Generator
      │
      ▼
Compiler
      │
      ▼
Fix Agent (if needed)
      │
      ▼
Renderer
      │
      ▼
Final Video
```

## Tech Stack

- Python
- LangGraph
- LangChain
- Google Gemini
- HuggingFace
- ChromaDB
- Remotion
- React
- TypeScript
- Node.js

## Project Structure

```
agents/
compiler/
generated/
models/
prompts/
rag/
remotion/
routers/
services/
state.py
graph.py
main.py
```

## Workflow

1. Parse user intent.
2. Analyze uploaded images using Vision AI.
3. Select the most relevant images.
4. Generate a storyboard.
5. Generate a Remotion React component.
6. Compile the generated code.
7. Automatically fix compilation errors if necessary.
8. Render the final video.

## Installation

```bash
git clone <repository>

cd image-to-video-multiagent-pipeline

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

npm install
```

## Run

```bash
python main.py
```

## Test Individual Modules

```bash
python test_image_loader.py
python test_image_utils.py
python test_storyboard_service.py
python test_remotion_service.py
python test_compiler.py
python test_renderer.py
```

## Output

```
generated/
    GeneratedVideo.tsx

output/
    final_video.mp4
```

## Future Improvements

- Background music generation
- AI voice narration
- Dynamic transitions
- Subtitle generation
- Automatic scene duration optimization
- Multi-language support
- Cloud rendering
- Advanced visual effects

## Author

Ayush Singh
