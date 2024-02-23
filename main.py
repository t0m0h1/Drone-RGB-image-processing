import cv2
import numpy as np


# This Python script is used to calculate the Visible Atmospherically Resistant Index (VARI) for an image and save the resulting VARI image.



def calculate_vari(image_path):
    # Read the orthomosaic map image
    image = cv2.imread(image_path)

    # Extract individual channels
    R, G, B = cv2.split(image)

    # Calculate VARI
    denominator = G + R - B + 1e-8  # Add a small constant to avoid division by zero
    VARI = (G.astype(float) - R.astype(float)) / denominator

    # Replace NaN or infinite values with zero
    VARI = np.nan_to_num(VARI)

    return VARI

def save_vari_image(vari, output_path):
    # Normalize VARI values to the range [0, 255] for display
    normalized_vari = cv2.normalize(vari, None, 0, 255, cv2.NORM_MINMAX)

    # Convert to uint8 for display and saving
    vari_display = normalized_vari.astype(np.uint8)

    # Save the VARI image
    cv2.imwrite(output_path, vari_display)

if __name__ == "__main__":
    # Input path for the orthomosaic map image
    ortho_image_path = "images/field.jpg"

    # Output path for the VARI image
    output_vari_path = "images/vari_field.jpg"

    # Calculate VARI
    vari_result = calculate_vari(ortho_image_path)

    # Save VARI image
    save_vari_image(vari_result, output_vari_path)
