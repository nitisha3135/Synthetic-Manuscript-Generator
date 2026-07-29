from PIL import ImageFilter, ImageEnhance
import random


def apply_effects(image):
    """
    Applies realistic manuscript effects.
    """

    # Slight blur (scan effect)
    if random.random() < 0.7:
        image = image.filter(
            ImageFilter.GaussianBlur(
                radius=random.uniform(0.2, 0.8)
            )
        )

    # Brightness variation
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(
        random.uniform(0.88, 1.08)
    )

    # Contrast variation
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(
        random.uniform(0.92, 1.12)
    )

    # Slight softening of digital text
    if random.random() < 0.6:
        image = image.filter(
            ImageFilter.GaussianBlur(0.3)
        )

    return image