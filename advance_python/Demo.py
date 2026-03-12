from PIL import Image, ImageDraw, ImageFont

# Your text
txt = """A SQL database table: SQL databases are designed to store structured data with a well-defined schema,
where each row represents a record and each column represents a field or attribute of that record."""

# Create blank image
img = Image.new('RGB', (800, 600), color=(255, 255, 255))
d = ImageDraw.Draw(img)

# Load a handwriting-like font (make sure you have one or download)
# font = ImageFont.truetype("Segoe Script.ttf", 18)  # Example font; replace with path to a handwriting font

# Write text
d.text((10, 10), txt, fill=(0, 0, 0))

# Save image
img.save("handwritten_output.png")
print("Image saved as handwritten_output.png")
