import os
from PIL import Image

# Update this to your folder path
input_folder = "/Users/burt/Documents/GitHub/Budget_Image_creator/assets/themes"
output_folder = os.path.join(input_folder, "cropped_4x5")

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def crop_to_4x5_and_resize(img, target_size=(1000, 1250)):
    width, height = img.size
    target_ratio = 4 / 5
    current_ratio = width / height

    if current_ratio > target_ratio:
        # Image too wide: crop width
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        box = (left, 0, left + new_width, height)
    else:
        # Image too tall: crop height
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        box = (0, top, width, top + new_height)

    cropped_img = img.crop(box)
    resized_img = cropped_img.resize(target_size, Image.LANCZOS)
    return resized_img

# Process images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        input_path = os.path.join(input_folder, filename)
        img = Image.open(input_path).convert("RGB")

        final_img = crop_to_4x5_and_resize(img)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

        final_img.save(output_path, "JPEG", quality=95)

print(f"✅ Done. Cropped and resized images saved in: {output_folder}")
