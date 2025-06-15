import imageio.v3 as iio
from PIL import Image
import numpy as np
import os

filenames = ['alice1.png', 'alice2.png', 'alice3.jpg', 'alice4.png', 'alice5.png']
images = []

# Set a target resolution (width, height)
target_size = (1920, 1080)

for filename in filenames:
    if os.path.exists(filename):
        img = Image.open(filename).convert("RGB").resize(target_size)
        images.append(np.array(img))
    else:
        print(f"❌ File not found: {filename}")

# Make GIF only if all images are loaded correctly
if images:
    iio.imwrite('alice.gif', images, duration=500, loop=0)
    print("✅ GIF created successfully!")
else:
    print("⚠️ No valid images loaded.")
