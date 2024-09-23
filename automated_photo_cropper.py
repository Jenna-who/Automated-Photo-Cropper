import os
from PIL import Image

# Path to the folder containing images
folder_path = 'your/folder/path'
output_folder = 'your/output/folder/path'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def crop_to_aspect_ratio(image, aspect_ratio=(16, 9)):
    img_width, img_height = image.size
    target_ratio = aspect_ratio[0] / aspect_ratio[1]
    
    # Determine which dimension is longer and crop based on that
    img_ratio = img_width / img_height
    if img_ratio > target_ratio:
        # If the image is wider than the target aspect ratio
        new_width = int(img_height * target_ratio)
        left = (img_width - new_width) // 2
        right = left + new_width
        return image.crop((left, 0, right, img_height))
    else:
        # If the image is taller than the target aspect ratio
        new_height = int(img_width / target_ratio)
        top = (img_height - new_height) // 2
        bottom = top + new_height
        return image.crop((0, top, img_width, bottom))

# Process all image files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        cropped_img = crop_to_aspect_ratio(img)
        cropped_img.save(os.path.join(output_folder, filename))

print(f"Images cropped and saved to {output_folder}")
