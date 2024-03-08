# RAF to WebP Converter
 RAF to WebP Converter python code

To create a generic version of the script and a corresponding README, I've abstracted the directory paths and included some customizable parameters to make the script more adaptable for different users and use cases.

### Generic Script

```python
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
```

### README

**RAF to WebP Converter**

This Python script is designed to automate the process of converting RAF files (raw images from Fujifilm cameras) to WebP format. It involves moving the RAF files from a source directory to an import directory, converting them to WebP format, and then cleaning up by removing the original RAF files.

**Requirements**

- Python 3.x
- `rawpy`: Used for reading RAF files and processing raw images.
- `Pillow` (PIL Fork): Used for converting processed images to WebP format.

You can install the required packages using pip:

```
pip install rawpy Pillow
```

**Usage**

1. Modify the `source_dir`, `import_dir`, and `webp_dir` variables in the script to match your directory paths:
- `source_dir`: The directory containing the original RAF files.
- `import_dir`: The directory where RAF files will be moved before processing.
- `webp_dir`: The directory where the converted WebP files will be saved.

2. Run the script:

```
python raf_to_webp_converter.py
```

**Note**: Ensure that you have the necessary read/write permissions for the directories you're using.

**Customization**

The script can be customized to handle different file formats or conversion settings by modifying the `raf_to_webp` function or adding new functions to suit your specific needs.