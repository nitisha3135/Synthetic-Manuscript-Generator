import os


def save_annotation(
    image_name,
    text,
    output_folder,
    script_name,
    font_name,
    background_name
):
    """
    Save detailed annotation.
    """

    md_name = image_name.replace(".png", ".md")

    md_path = os.path.join(output_folder, md_name)

    with open(md_path, "w", encoding="utf-8") as f:

        f.write("# Synthetic Manuscript Annotation\n\n")

        f.write(f"**Image:** {image_name}\n\n")

        f.write(f"**Script:** {script_name}\n\n")

        f.write(f"**Font:** {font_name}\n\n")

        f.write(f"**Background:** {background_name}\n\n")

        f.write("## Text\n\n")

        f.write(text)