from pathlib import Path
import webview

BASE_DIR = Path(__file__).resolve().parent
NOTE_PATH = BASE_DIR / "memo.txt"


class MemoApi:

    def __init__(self):
        pass

    def save_note(self, text):

        NOTE_PATH.write_text(
            text,
            encoding="utf-8"
        )

        return {
            "status": "saved",
            "path": str(NOTE_PATH)
        }

    def load_note(self):

        if NOTE_PATH.exists():
            return NOTE_PATH.read_text(
                encoding="utf-8"
            )

        return ""


def main():

    html_file = (
        BASE_DIR / "text.html"
    ).as_uri()

    print("현재 읽는 HTML 파일:")
    print(html_file)

    webview.create_window(
        "Simple Memo",
        url=html_file,
        js_api=MemoApi(),
        width=800,
        height=600,
        resizable=True
    )

    webview.start()


if __name__ == "__main__":
    main()