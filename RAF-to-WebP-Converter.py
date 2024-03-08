import os
import shutil
import rawpy
from PIL import Image

def raf_to_webp(raf_file_path, webp_file_path):
    """Convert RAF files to WebP format."""
    with rawpy.imread(raf_file_path) as raw:
        rgb = raw.postprocess()
    img = Image.fromarray(rgb)
    img.save(webp_file_path, format='WEBP', lossless=True)

def process_files(source_dir, import_dir, webp_dir):
    """Process RAF files: move, convert to WebP, and clean up."""
    # Ensure the target directories exist
    if not os.path.exists(import_dir):
        os.makedirs(import_dir)
    if not os.path.exists(webp_dir):
        os.makedirs(webp_dir)

    # Move .raf files from source to import_dir
    for filename in os.listdir(source_dir):
        if filename.lower().endswith('.raf'):
            raf_file_path = os.path.join(source_dir, filename)
            imported_file_path = os.path.join(import_dir, filename)
            shutil.move(raf_file_path, imported_file_path)

    # Process files in import_dir and save them to webp_dir
    for filename in os.listdir(import_dir):
        if filename.lower().endswith('.raf'):
            raf_file_path = os.path.join(import_dir, filename)
            webp_file_path = os.path.join(webp_dir, filename.rsplit('.', 1)[0] + '.webp')
            raf_to_webp(raf_file_path, webp_file_path)

            # Remove the original .raf file from import_dir
            os.remove(raf_file_path)
            print(f"Processed and removed: {filename}")

# Example usage
source_dir = 'path/to/source'
import_dir = 'path/to/import'
webp_dir = 'path/to/webp'

process_files(source_dir, import_dir, webp_dir)
