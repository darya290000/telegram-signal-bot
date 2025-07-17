import zipfile
import os

def zip_project(output_filename="project.zip"):
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("."):
            for file in files:
                if file == output_filename:
                    continue  # فایل خودش را zip نکند
                filepath = os.path.join(root, file)
                zipf.write(filepath, filepath)

zip_project()
print("✅ پروژه با موفقیت فشرده شد: project.zip")
