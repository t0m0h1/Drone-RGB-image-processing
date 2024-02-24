import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_vari(image_path):
    image = cv2.imread(image_path)
    Blue, Green, Red = cv2.split(image)
    
    # Adding a small constant to avoid division by zero
    denominator = (Green + Red - Blue) + 0.001
    VARi = (Green - Red) / denominator
    
    VARi = np.nan_to_num(VARi)
    return VARi

def save_vari_image(vari, output_path):
    # Clip the VARi values to the range [-1, 1] for better visualization
    normalized_vari = np.clip(vari, -1, 1)

    # Create a custom color map with green for positive values and red for negative values
    cmap = plt.cm.RdYlGn

    # Normalize colormap to the range [0, 1]
    norm = plt.Normalize(vmin=-1, vmax=1)

    # Apply the colormap to the normalized VARi values
    vari_display = (cmap(norm(normalized_vari)) * 255).astype(np.uint8)

    cv2.imwrite(output_path, vari_display)

if __name__ == "__main__":
    ortho_image_path = "images/field.jpg"
    output_vari_path = "images/vari_field_map.jpg"
    vari_result = calculate_vari(ortho_image_path)
    save_vari_image(vari_result, output_vari_path)
    print("VARi crop health map saved to", output_vari_path)
