import cv2
import numpy as np
import matplotlib.pyplot as plt

def identify_vegetation(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image file not found at {image_path}")

    # Convert the image to HSV color space
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define range for green color in HSV with increased sensitivity
    lower_green = np.array([30, 70, 50])  # Lower bound for green (slightly wider hue)
    upper_green = np.array([90, 255, 255])  # Upper bound for green (slightly wider hue)

    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(image_hsv, lower_green, upper_green)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Increase the intensity of the green color
    result[:,:,1] = np.clip(result[:,:,1] + 50, 0, 255)

    # Convert non-vegetation areas to red
    non_vegetation_mask = cv2.bitwise_not(mask)
    result[non_vegetation_mask > 0] = [0, 0, 255]  # Change to red in BGR

    return result

def display_and_save_result(result, output_path):
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
    plt.axis('off')
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.show()

if __name__ == "__main__":
    input_image_path = 'images/field2.jpg'
    output_image_path = 'images/output.jpg'
    result_image = identify_vegetation(input_image_path)
    display_and_save_result(result_image, output_image_path)
    print(f"Output image saved to {output_image_path}")
