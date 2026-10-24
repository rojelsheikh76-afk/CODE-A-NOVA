from pathlib import Path
import shutil

BASE_DIR = Path(__file__).parent
SOURCE_DIR = BASE_DIR / "test_files"

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
    "Code": [".py", ".java", ".cpp", ".html"],
}

def get_category(file_path):
    for category, extensions in CATEGORIES.items():
        if file_path.suffix.lower() in extensions:
            return category
    return "Others"

def organize_files():
    if not SOURCE_DIR.exists():
        print("Error: Source folder does not exist.")
        return

    moved = 0

    for file_path in SOURCE_DIR.iterdir():
        if not file_path.is_file():
            continue

        category = get_category(file_path)
        target_dir = SOURCE_DIR / category
        target_dir.mkdir(exist_ok=True)

        destination = target_dir / file_path.name

        counter = 1
        while destination.exists():
            destination = target_dir / (
                f"{file_path.stem}_{counter}{file_path.suffix}"
            )
            counter += 1

        shutil.move(str(file_path), str(destination))
        print(f"Moved: {file_path.name} -> {category}/")
        moved += 1

    print(f"\nOrganization complete! Files moved: {moved}")

if __name__ == "__main__":
    print("CODE-A-NOVA FILE ORGANIZER")
    print(f"Source folder: {SOURCE_DIR}")
    organize_files()
