from PIL import Image
from PIL import ImageEnhance
import numpy as np

def negative_to_positive(input_path, output_path):
    # Open the image
    img = Image.open(input_path)

    # Convert image to numpy array
    img_array = np.array(img)
    
    # Invert the colors
    #inverted_array = 255 - img_array
    inverted_array = img_array
    
    # Create a new image from the inverted array
    inverted_img = Image.fromarray(inverted_array)
    
    
    # Adjust color balance (this is a simple method and may need fine-tuning)
    r, g, b = inverted_img.split()
    #r = source[r].point(lambda i: 10 < i < 250 )
    r = r.point(lambda i: i * 1.0)
    g = g.point(lambda i: i * 1.0)
    #g = g.point(lambda i: 0 < i < 255 )
    b = b.point(lambda i: i * 1.0)
    
    # Merge the color channels
    result = Image.merge('RGB', (r, g, b))

    # Enhance brightness by 0.8
    enhancer = ImageEnhance.Brightness(result)
    result = enhancer.enhance(1.3)
    
    # Save the result
    result.save(output_path)

# Usage
source = "C:/Users/Johan/Bilder_C/negativ/Skanning_20240908.png"
target = "C:/Users/Johan/Bilder_C/negativ/ready_files/Skanning_reultat.png"
negative_to_positive(source, target)