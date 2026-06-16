import os
import shutil

# Folder you want to organize
TARGET_FOLDER = "test_folder"

# File type categories based on extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"],
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    moved_count = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(filename)
        category = get_category(extension)

        category_folder = os.path.join(folder_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        destination = os.path.join(category_folder, filename)
        shutil.move(file_path, destination)
        print(f"Moved '{filename}' -> {category}/")
        moved_count += 1

    if moved_count == 0:
        print("No files to organize.")
    else:
        print(f"\nDone! Organized {moved_count} file(s).")

if __name__ == "__main__":
    organize_folder(TARGET_FOLDER)