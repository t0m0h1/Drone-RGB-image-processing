import cv2
import numpy as np

def calculate_vari(image_path):
    image = cv2.imread(image_path)
    R, G, B = cv2.split(image)
    denominator = G + R - B + 1e-8
    VARI = (G.astype(float) - R.astype(float)) / denominator
    VARI = np.nan_to_num(VARI)
    return VARI

def save_vari_image(vari, output_path):
    # Normalize VARI values to the range [0, 1] for mapping
    normalized_vari = (vari - np.min(vari)) / (np.max(vari) - np.min(vari) + 1e-8)

    # Create a custom color map
    colors = [(0, 0, 255), (0, 255, 0)]  # BGR format
    cmap = np.linspace(colors[0], colors[1], 256).astype(np.uint8)

    # Apply the custom color map using cv2.applyColorMap
    vari_display = cv2.applyColorMap((normalized_vari * 255).astype(np.uint8), cmap)

    cv2.imwrite(output_path, vari_display)

if __name__ == "__main__":
    ortho_image_path = "images/field.jpg"
    output_vari_path = "images/vari_field.jpg"
    vari_result = calculate_vari(ortho_image_path)
    save_vari_image(vari_result, output_vari_path)
    print("VARI image saved to", output_vari_path)