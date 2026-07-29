from PIL import Image, ImageDraw, ImageFont
import random


def wrap_line(draw, text, font, max_width):
    """Wrap a single line so it never exceeds max_width."""
    words = text.split()

    if not words:
        return []

    wrapped = []
    current = words[0]

    for word in words[1:]:

        trial = current + " " + word

        bbox = draw.textbbox((0, 0), trial, font=font)
        width = bbox[2] - bbox[0]

        if width <= max_width:
            current = trial
        else:
            wrapped.append(current)
            current = word

    wrapped.append(current)

    return wrapped


def render_text(background_path, font_path, lines):

    image = Image.open(background_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    width, height = image.size

    # Smaller font
    font_size = random.randint(14, 17)

    font = ImageFont.truetype(font_path, font_size)

    left_margin = 35
    right_margin = 35
    top_margin = 30
    bottom_margin = 30

    max_width = width - left_margin - right_margin

    line_spacing = random.randint(18, 22)

    y = top_margin

    ink_colors = [
        (60,40,20),
        (70,45,25),
        (80,50,28),
        (90,60,35)
    ]

    for original in lines:

        original = original.strip()

        if not original:
            continue

        wrapped_lines = wrap_line(
            draw,
            original,
            font,
            max_width
        )

        for line in wrapped_lines:

            if y > height - bottom_margin:
                return image

            x = left_margin + random.randint(-3,3)

            draw.text(
                (x,y),
                line,
                font=font,
                fill=random.choice(ink_colors)
            )

            y += line_spacing

    return image