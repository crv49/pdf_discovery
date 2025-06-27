import os
import random
import shutil

# Paths
base_dir = 'data'
image_dir = os.path.join(base_dir, 'train/images')
label_dir = os.path.join(base_dir, 'train/labels')

# Output folders
splits = ['train', 'val', 'test']
ratios = {'train': 0.7, 'val': 0.15, 'test': 0.15}

for split in splits:
    os.makedirs(os.path.join(base_dir, split, 'images'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, split, 'labels'), exist_ok=True)

# Get and shuffle images
image_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]
random.shuffle(image_files)

# Split
total = len(image_files)
train_end = int(ratios['train'] * total)
val_end = train_end + int(ratios['val'] * total)

split_data = {
    'train': image_files[:train_end],
    'val': image_files[train_end:val_end],
    'test': image_files[val_end:]
}

# Move files
for split, files in split_data.items():
    for image_file in files:
        label_file = image_file.replace('.png', '.txt')

        # Paths
        src_img = os.path.join(image_dir, image_file)
        src_lbl = os.path.join(label_dir, label_file)
        dst_img = os.path.join(base_dir, split, 'images', image_file)
        dst_lbl = os.path.join(base_dir, split, 'labels', label_file)

        shutil.move(src_img, dst_img)
        if os.path.exists(src_lbl):
            shutil.move(src_lbl, dst_lbl)
        else:
            print(f"[WARNING] No label for {image_file}")

print("Split complete.")
