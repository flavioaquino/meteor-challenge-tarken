from PIL import Image, ImageDraw

def generate_meteor_image(image_path, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to RGB mode (if not already in RGB)
    img = img.convert("RGB")

    # Get the image size
    width, height = img.size

    # Create a new image with the same dimensions as the original image
    meteor_img = Image.new("RGB", (width, height), color="black")

    # Initialize a drawing context
    draw = ImageDraw.Draw(meteor_img)

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the current pixel
            pixel = img.getpixel((x, y))

            # Check for meteors (pure red pixels)
            if pixel == (255, 0, 0):
                # Search for blue pixels in the same Y-coordinate
                for yy in range(y + 1, height):
                    pixel_below = img.getpixel((x, yy))
                    if pixel_below == (0, 0, 255):  # pure blue
                        # Draw the meteor pixel on the new image
                        draw.point((x, y), fill=(255, 0, 0))
                        break  # Stop searching once a blue pixel is found
                    elif pixel_below == (255, 255, 255):  # pure white (star)
                        break  # Stop searching if a star is encountered
                    elif pixel_below == (0, 0, 0):  # pure black (ground)
                        break  # Stop searching if ground is encountered
                    elif pixel_below == (255, 0, 0):  # pure red (meteor)
                        break  # Stop searching if another meteor is encountered

    # Save the generated image
    meteor_img.save(output_path)

def analyze_image(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to RGB mode (if not already in RGB)
    img = img.convert("RGB")

    # Get the image size
    width, height = img.size

    # Initialize counts
    stars_count = 0
    meteors_count = 0
    meteors_on_water_count = 0
    hidden_phrase = ""

    # Threshold to determine if a meteor is falling on water
    water_threshold = height * 0.02  # Adjust as needed

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the current pixel
            pixel = img.getpixel((x, y))

            # Check for stars
            if pixel == (255, 255, 255):  # pure white
                stars_count += 1

            # Check for meteors
            elif pixel == (255, 0, 0):  # pure red
                meteors_count += 1

                # Search for blue pixels in the same Y-coordinate
                for yy in range(y + 1, height):
                    pixel_below = img.getpixel((x, yy))
                    if pixel_below == (0, 0, 255):  # pure blue
                        meteors_on_water_count += 1
                        break  # Stop searching once a blue pixel is found
                    elif pixel_below == (255, 255, 255):  # pure white (star)
                        break  # Stop searching if a star is encountered
                    elif pixel_below == (0, 0, 0):  # pure black (ground)
                        break  # Stop searching if ground is encountered
                    elif pixel_below == (255, 0, 0):  # pure red (meteor)
                        break  # Stop searching if another meteor is encountered

            # Check for hidden phrase
            elif pixel == (0, 0, 0):  # pure black (ground)
                # Assuming the hidden phrase is encoded in the dots in the sky
                hidden_phrase += chr(ord('A') + (x % 26))  # Map x-coordinate to letters A-Z

    return stars_count, meteors_count, meteors_on_water_count, hidden_phrase

output_image_path = "falling_meteors.png"
image_path = "meteor_challenge_01.png"
input_image_path = "meteor_challenge_01.png"
stars, meteors, meteors_on_water, hidden_phrase = analyze_image(image_path)

print("Number of Stars:", stars)
print("Number of Meteors:", meteors)
print("Number of Meteors falling on Water:", meteors_on_water)
print("Hidden Phrase:", hidden_phrase)

generate_meteor_image(input_image_path, output_image_path)

print("Image containing only the falling meteors has been generated:", output_image_path)
