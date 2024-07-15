from PIL import Image, ImageDraw

# Create a new image with white background
img = Image.new('RGB', (100, 100), color = (100, 150, 30))

# Initialize the drawing context
d = ImageDraw.Draw(img)

# Draw a black rectangle
d.rectangle([10, 10, 90, 90], outline="black", fill="black")

# Save the image
img.save('image.png')