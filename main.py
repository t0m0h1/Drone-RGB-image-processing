import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_savi(image_path):
    image = cv2.imread(image_path)
    R, G, B = cv2.split(image)
    denominator = G + R + 0.5  # Adding 0.5 to avoid division by zero
    SAVI = ((G - R) / denominator) * 1.5
    SAVI = np.nan_to_num(SAVI)
    return SAVI

def save_savi_image(savi, output_path):
    # Clip the SAVI values to the range [0, 1]
    normalized_savi = np.clip(savi, 0, 1)

    # Display histogram to understand the distribution of SAVI values
    plt.hist(normalized_savi.flatten(), bins=50, color='c', edgecolor='k', alpha=0.7)
    plt.title('SAVI Distribution')
    plt.xlabel('Normalized SAVI Values')
    plt.ylabel('Frequency')
    plt.show()

    # Create a custom color map with green emphasis
    cmap = plt.get_cmap('viridis')

    # Apply the custom color map using cv2.applyColorMap
    savi_display = (cmap(normalized_savi) * 255).astype(np.uint8)

    cv2.imwrite(output_path, savi_display)

if __name__ == "__main__":
    ortho_image_path = "images/field.jpg"
    output_savi_path = "images/savi_field_green.jpg"
    savi_result = calculate_savi(ortho_image_path)
    save_savi_image(savi_result, output_savi_path)
    print("SAVI image saved to", output_savi_path)
