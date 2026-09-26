from pathlib import Path
import shutil, argparse

CATEGORIES = {
    "Images": {".png",".jpg",".jpeg",".gif",".webp"},
    "Documents": {".pdf",".docx",".doc",".txt",".xlsx",".pptx",".csv"},
    "Videos": {".mp4",".mkv",".mov",".avi"},
    "Audio": {".mp3",".wav",".aac"},
    "Archives": {".zip",".rar",".7z"},
    "Code": {".py",".js",".html",".css",".java",".cpp",".c"}
}

def organize(folder):
    folder = Path(folder).expanduser().resolve()
    if not folder.is_dir():
        raise ValueError("Folder does not exist.")
    moved = 0
    for file in folder.iterdir():
        if not file.is_file() or file.name == Path(__file__).name:
            continue
        category = next((c for c, exts in CATEGORIES.items()
                         if file.suffix.lower() in exts), "Others")
        target_dir = folder / category
        target_dir.mkdir(exist_ok=True)
        target = target_dir / file.name
        n = 1
        while target.exists():
            target = target_dir / f"{file.stem}_{n}{file.suffix}"
            n += 1
        shutil.move(str(file), str(target))
        moved += 1
    print(f"Done! Organized {moved} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="Folder to organize")
    args = parser.parse_args()
    organize(args.folder)
