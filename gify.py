import sys
from PIL import Image
import os

with_crop = len(sys.argv) > 2
if len(sys.argv) < 2:
    print("Usage: python gify.py folder_path <left_x upper_y right_x lower_y>")
    exit(1)

folder_path = sys.argv[1]

if with_crop:
    left = int(sys.argv[2])
    upper = int(sys.argv[3])
    right = int(sys.argv[4])
    lower = int(sys.argv[5])

# Validate if the folder path exists
if not os.path.exists(folder_path):
    print(f"The folder path '{folder_path}' does not exist.")
    exit(1)

png_files = [file for file in os.listdir(folder_path) if file.endswith(".png")]

png_files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

images = []


for png_file in png_files:
    img = Image.open(os.path.join(folder_path, png_file))
    if with_crop:
        cropped_img = img.crop((left, upper, right, lower))
        images.append(cropped_img)
    else:
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