import cv2
import numpy as np
import matplotlib.pyplot as plt

def identify_vegetation(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image file not found at {image_path}")
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define range for green color in RGB
    lower_green = np.array([0, 50, 0])
    upper_green = np.array([150, 255, 150])

    # Threshold the RGB image to get only green colors
    mask = cv2.inRange(image_rgb, lower_green, upper_green)

    # Apply the mask to the original image
    result = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)

    # Increase the intensity of the green color
    result[:,:,1] = np.clip(result[:,:,1] + 50, 0, 255)

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
    input_image_path = 'images/field2.jpg'
    output_image_path = 'images/output.jpg'
    result_image = identify_vegetation(input_image_path)
    display_and_save_result(result_image, output_image_path)
    print(f"Output image saved to {output_image_path}")