import cv2
import numpy as np
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

def preprocess_savi(savi):
    # Apply preprocessing to handle skewed data
    preprocessed_savi = np.log1p(savi)
    return preprocessed_savi

def save_savi_image(savi, output_path):
    # Clip the SAVI values to the range [0, 1]
    normalized_savi = np.clip(savi, 0, 1)

    # Display histogram to understand the distribution of SAVI values
    plt.hist(normalized_savi.flatten(), bins=50, color='c', edgecolor='k', alpha=0.7)
    plt.title('SAVI Distribution')
    plt.xlabel('Normalized SAVI Values')
    plt.ylabel('Frequency')
    plt.show()

    # Create a custom color map with 256 colors
    colors = [(0, 0, 255), (0, 255, 0)]  # BGR format
    cmap = np.linspace(colors[0], colors[1], 256).astype(np.uint8)

    # Apply the custom color map using cv2.applyColorMap
    savi_display = cv2.applyColorMap((normalized_savi * 255).astype(np.uint8), cv2.COLORMAP_JET)

    # Turn up the intensity of the green channel
    savi_display[:, :, 1] = np.clip(savi_display[:, :, 1] * 1.2, 0, 255).astype(np.uint8)  # Multiply green channel values by 1.2

    cv2.imwrite(output_path, savi_display)




    

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ortho_image_path = "images/field2.jpg"
    output_savi_path = "images/savi_field.jpg"
    savi_result = calculate_savi(ortho_image_path)
    preprocessed_savi = preprocess_savi(savi_result)
    save_savi_image(preprocessed_savi, output_savi_path)
    print("SAVI image saved to", output_savi_path)

    # Plot the vegetation using matplotlib
    plt.imshow(preprocessed_savi, cmap='Greens')
    plt.title('Vegetation')
    plt.colorbar(label='Normalized SAVI Values')
    plt.show()






