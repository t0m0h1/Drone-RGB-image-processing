import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def identify_vegetation(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define a range for green color (you may need to adjust these values based on your images)
    lower_green = np.array([0, 100, 0], dtype=np.uint8)
    upper_green = np.array([50, 255, 50], dtype=np.uint8)

    # Create a mask for green pixels
    mask = cv2.inRange(image_rgb, lower_green, upper_green)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)

    # Convert non-vegetation areas to red
    non_vegetation_mask = cv2.bitwise_not(mask)
    result[non_vegetation_mask > 0] = [255, 0, 0]

    return result

def display_and_save_result(result, output_path):
    plt.imshow(result)
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.show()

if __name__ == "__main__":
    # Replace 'your_image_path.jpg' with the path to your input image
    input_image_path = '.images/field2.jpg'
    
    # Get the directory of the input image
    input_dir = os.path.dirname(os.path.abspath(input_image_path))
    
    # Define the output path as 'output.jpg' in the same directory
    output_image_path = os.path.join(input_dir, 'output.jpg')

    result_image = identify_vegetation(input_image_path)
    display_and_save_result(result_image, output_image_path)
