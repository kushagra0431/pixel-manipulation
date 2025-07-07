from PIL import Image
import numpy as np

def encrypt_decrypt_image(input_path, output_path, key):
    # Open the image and convert to RGB
    img = Image.open(input_path).convert('RGB')
    img_array = np.array(img)
    
    # Apply XOR operation to each pixel with the key
    encrypted_array = img_array ^ key
    
    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Processed image saved as {output_path}")

# Usage Example
if __name__ == "__main__":
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    in_file = input("Enter input image path: ")
    out_file = input("Enter output image path: ")
    key = int(input("Enter encryption key (0-255): "))
    
    encrypt_decrypt_image(in_file, out_file, key)



