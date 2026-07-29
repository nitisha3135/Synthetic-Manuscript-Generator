import os
import shutil

SOURCE_FOLDER = "output"
DESTINATION_FOLDER = "dataset"

TRAIN = 85
VALIDATION = 10
TEST = 5

SCRIPTS = [
    "devanagari",
    "modi",
    "sharada"
]

for script in SCRIPTS:

    source = os.path.join(SOURCE_FOLDER, script)

    train_folder = os.path.join(
        DESTINATION_FOLDER,
        "train",
        script
    )

    validation_folder = os.path.join(
        DESTINATION_FOLDER,
        "validation",
        script
    )

    test_folder = os.path.join(
        DESTINATION_FOLDER,
        "test",
        script
    )

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(validation_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    images = sorted([
        file
        for file in os.listdir(source)
        if file.endswith(".png")
    ])

    train_images = images[:TRAIN]
    validation_images = images[TRAIN:TRAIN + VALIDATION]
    test_images = images[TRAIN + VALIDATION:]

    def copy_dataset(files, destination):

        for image in files:

            md = image.replace(".png", ".md")

            shutil.copy(
                os.path.join(source, image),
                os.path.join(destination, image)
            )

            shutil.copy(
                os.path.join(source, md),
                os.path.join(destination, md)
            )

    copy_dataset(train_images, train_folder)
    copy_dataset(validation_images, validation_folder)
    copy_dataset(test_images, test_folder)

    print(f"{script} ✔")

print("\nDataset successfully split!")