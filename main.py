from config import settings
from utils.logger import console

def main():

    console.print("[green]Image-to-Video Multi-Agent Pipeline[/green]")

    console.print(f"Retry Limit : {settings.RETRY_LIMIT}")

    console.print(f"Assets Folder : {settings.IMAGE_FOLDER}")

if __name__=="__main__":
    main()