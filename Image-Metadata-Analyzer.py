import os
from datetime import datetime
from PIL import Image
import pandas as pd

# Folder where your JPG files are uploaded
folder_path = r"C:\Users\Kishore\test_images"



def analyze_images(folder_path):
    metadata = []

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Check for JPG / PNG / JPEG
        if os.path.isfile(file_path) and file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            try:
                with Image.open(file_path) as img:
                    file_stats = os.stat(file_path)

                    metadata.append({
                        "File Name": file_name,
                        "Format": img.format,
                        "Mode": img.mode,
                        "Width": img.width,
                        "Height": img.height,
                        "File Size (KB)": round(file_stats.st_size / 1024, 2),
                        "Created On": datetime.fromtimestamp(file_stats.st_ctime),
                        "Modified On": datetime.fromtimestamp(file_stats.st_mtime),
                    })
            except Exception:
                print(f"Skipping {file_name} (corrupted or unreadable)")

    df = pd.DataFrame(metadata)
    df.to_csv("image_metadata.csv", index=False)
    print("\n✔ Metadata saved to image_metadata.csv")

    return df


# Run the analysis
df = analyze_images(folder_path)
df
