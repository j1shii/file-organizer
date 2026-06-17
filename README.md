# File Organizer

A Python automation script that automatically sorts files in a folder into categorized subfolders based on file type.

## What it does

Scans a target folder and moves files into subfolders:
- Images (.jpg, .jpeg, .png, .gif, .bmp, .svg)
- Documents (.pdf, .docx, .doc, .txt, .xlsx, .pptx)
- Videos (.mp4, .mov, .avi, .mkv)
- Audio (.mp3, .wav, .aac)
- Archives (.zip, .rar, .7z, .tar, .gz)
- Code (.py, .js, .html, .css, .java, .c, .cpp)
- Others (anything that doesn't match the above)

## Tech used

- Python
- `os` module (file system navigation)
- `shutil` module (file moving)

## Concepts demonstrated

- File I/O and automation
- Dictionary-based category
