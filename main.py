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
    min_val = np.min(vari)
    max_val = np.max(vari)
    normalized_vari = 255 * (vari - min_val) / (max_val - min_val)
    normalized_vari = np.clip(normalized_vari, 0, 255)
    vari_display = normalized_vari.astype(np.uint8)

    # Convert to 3-channel image
    vari_display = cv2.cvtColor(vari_display, cv2.COLOR_GRAY2BGR)

    # Create a custom color map
    colors = [(0, 0, 255), (0, 255, 0)]  # BGR format
    cmap = np.linspace(colors[0], colors[1], 256).astype(np.uint8)

    # Apply the custom color map
    vari_display = cv2.LUT(vari_display, cmap)

    cv2.imwrite(output_path, vari_display)

if __name__ == "__main__":
    ortho_image_path = "images/field.jpg"
    output_vari_path = "images/vari_field.jpg"
    vari_result = calculate_vari(ortho_image_path)
    save_vari_image(vari_result, output_vari_path)