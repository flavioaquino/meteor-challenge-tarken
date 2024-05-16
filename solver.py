from PIL import Image

def count_red_blue_and_white_pixels(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to RGB mode (if not already in RGB)
    img = img.convert("RGB")

    # Get the image size
    width, height = img.size

    # Initialize counts of red, blue, and white pixels
    red_pixel_count = 0
    blue_pixel_count = 0
    white_pixel_count = 0

    # Iterate through each pixel
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the current pixel
            pixel = img.getpixel((x, y))

            # Check if the pixel is red
            if isinstance(pixel, tuple) and len(pixel) == 3:
                r, g, b = pixel
                if r > 250 and g < 100 and b < 100:
                    red_pixel_count += 1
                    alt = y
                    for alt in range(alt, height):
                        pixel = img.getpixel((x, alt))
                        r, g, b = pixel
                        if r < 100 and g < 100 and b > 250:
                            blue_pixel_count += 1
                            break

            # Check if the pixel is pure white
            if pixel == (255, 255, 255):
                white_pixel_count += 1

    return red_pixel_count, blue_pixel_count, white_pixel_count

image_path = "meteor_challenge_01.png"
red_count, blue_count, white_count = count_red_blue_and_white_pixels(image_path)
print("Number of meteors:", red_count)
print("Number of falling meteors:", blue_count)
print("Number of stars:", white_count)
