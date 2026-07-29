import os
import random

from renderer import render_text
from effects import apply_effects
from annotations import save_annotation

# ----------------------------
# Configuration
# ----------------------------

OUTPUT_FOLDER = "output"
BACKGROUND_FOLDER = "backgrounds"

SCRIPTS = {
    "devanagari": {
        "text": "scripts/devanagari_md.md",
        "font": "fonts/NotoSansDevanagari-Regular.ttf"
    },

    "modi": {
        "text": "scripts/Modi_md.md",
        "font": "fonts/NotoSansModi-Regular.ttf"
    },

    "sharada": {
        "text": "scripts/sharada_md.md",
        "font": "fonts/NotoSansSharada-Regular.ttf"
    }
}

IMAGES_PER_SCRIPT = 100

backgrounds = [
    os.path.join(BACKGROUND_FOLDER, f)
    for f in os.listdir(BACKGROUND_FOLDER)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

if not backgrounds:
    raise Exception("No backgrounds found!")

for script_name, data in SCRIPTS.items():

    print(f"\nGenerating {script_name} dataset...")

    output_dir = os.path.join(OUTPUT_FOLDER, script_name)

    os.makedirs(output_dir, exist_ok=True)

    with open(data["text"], "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    for i in range(1, IMAGES_PER_SCRIPT + 1):

        start = random.randint(0, max(0, len(lines) - 10))

        page_lines = lines[start:start + random.randint(10,16)]

        text = "\n".join(page_lines)

        bg = random.choice(backgrounds)
        
        image = render_text(
            background_path=bg,
            font_path=data["font"],
            lines=page_lines
        )

        image = apply_effects(image)

        image_name = f"{script_name}_{i:03d}.png"

        image.save(
            os.path.join(output_dir, image_name)
        )
        
        save_annotation(
            image_name=image_name,
            text=text,
            output_folder=output_dir,
            script_name=script_name,
            font_name=os.path.basename(data["font"]),
            background_name=os.path.basename(bg)
        )

    print(f"{script_name} completed!")

print("\nAll datasets generated successfully!")