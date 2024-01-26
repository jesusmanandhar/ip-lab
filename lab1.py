from PIL import Image

# Read image
input_image_path = 'me.jpg'
image = Image.open(input_image_path)

# Display image
image.show()

# Save image
output_image_path = 'output_image.jpg'
image.save(output_image_path)
print(f"Image saved successfully at {output_image_path}")
