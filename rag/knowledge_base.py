from pathlib import Path


STYLE_FOLDER = Path("rag/style_guides")
REMOTION_FOLDER = Path("rag/remotion_docs")


def load_documents():

    documents = []

    folders = [
        STYLE_FOLDER,
        REMOTION_FOLDER
    ]

    for folder in folders:

        for file in folder.glob("*.txt"):

            text = file.read_text(
                encoding="utf-8"
            )

            documents.append(

                {
                    "id": file.stem,
                    "document": text,
                    "source": folder.name
                }

            )

    return documents