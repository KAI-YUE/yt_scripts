from PIL import Image, ImageDraw, ImageFont

def split_text_to_lines(text, font, draw, image_width, padding=20):
    """
    Splits text into lines, ensuring each line fits within the specified width.
    """
    words = text.split()
    lines = []
    current_line = []
    
    for word in words:
        # Check if adding the next word exceeds the line width
        test_line = ' '.join(current_line + [word])
        width, _ = draw.textsize(test_line, font=font)
        if width <= image_width - padding:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    
    # Add the last line
    lines.append(' '.join(current_line))
    return lines


def load_or_create_image(image_path, image_size=(1920, 1080)):
    """
    Load a user-specified image if provided, or create a blank image.
    """
    if image_path:
        try:
            img = Image.open(image_path)
            img = img.resize(image_size)  # Resize for consistency
        except Exception as e:
            print(f"Error loading image: {e}. Creating a blank image instead.")
            img = Image.new('RGB', image_size, color=(0, 0, 0))
    else:
        img = Image.new('RGB', image_size, color=(0, 0, 0))
    return img


def create_caption_image_with_base(text, base_image_path=None, image_size=(1920, 1080), save_path="caption_with_base.png", font_path=None, font_size=60):
    # Convert text to AMA title case
    text = convert_to_ama_title_case(text)
    
    # Load base image or create a blank one
    img = load_or_create_image(base_image_path, image_size)
    draw = ImageDraw.Draw(img)
    
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        # Use a default font for demonstration, adjust as needed
        font = ImageFont.load_default()
    
    lines = split_text_to_lines(text, font, draw, image_size[0])
    text_height_total = len(lines) * font_size  # Adjust vertical spacing based on line count and font size
    
    # Dynamically adjust font size if necessary
    while text_height_total > image_size[1] - 40 and font_size > 10:
        font_size -= 1
        if font_path:
            font = ImageFont.truetype(font_path, font_size)
        lines = split_text_to_lines(text, font, draw, image_size[0])
        text_height_total = len(lines) * font_size
    
    # Calculate starting Y position
    y = (image_size[1] - text_height_total) / 2
    
    # Draw each line
    for line in lines:
        line_width, line_height = draw.textsize(line, font=font)
        x = (image_size[0] - line_width) / 2
        draw.text((x, y), line, font=font, fill=(255, 255, 255))
        y += font_size
    
    # Save the image with caption
    img.save(save_path)
    
    return save_path


def convert_to_ama_title_case(text):
    # List of words to lowercase (simple approximation)
    lowercase_words = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'from', 'by']
    # Split the text into words and capitalize appropriately
    final_title = []
    words = text.strip().split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in lowercase_words:
            final_title.append(word.capitalize())
        else:
            final_title.append(word.lower())
    return ' '.join(final_title)

# Example usage

save_path = "/home/kyue/Pictures/tmp/caption_default_font.png"
font_path = "/mnt/win-ssd/Users/youtube+pics/nowhand_drawing/drawing-guides-font/chalk.ttf"
font_size = 140

subtitle_text = "I love chloe"
caption_default_font_path = create_caption_image_with_base(subtitle_text, save_path=save_path, font_path=font_path, font_size=font_size)
print(f"Caption image saved at: {caption_default_font_path}")
