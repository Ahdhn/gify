import sys
from PIL import Image
import os

if len(sys.argv) != 2:
    print("Usage: python gify.py <folder_path>")
    exit(1)

folder_path = sys.argv[1]

# Validate if the folder path exists
if not os.path.exists(folder_path):
    print(f"The folder path '{folder_path}' does not exist.")
    exit(1)

png_files = [file for file in os.listdir(folder_path) if file.endswith(".png")]

png_files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

images = []


for png_file in png_files:
    img = Image.open(os.path.join(folder_path, png_file))
    images.append(img)

output_gif = os.path.join(folder_path, "output.gif")

images[0].save(
    output_gif,
    save_all=True,
    append_images=images[1:],
    duration=300,  # Set the duration between frames in milliseconds (adjust as needed)
    loop=0,  # 0 means loop forever, or set to a specific number of loops
    optimize=False,  # Disable GIF optimization/compression
)


print(f"Successfully created '{output_gif}' in the folder.")