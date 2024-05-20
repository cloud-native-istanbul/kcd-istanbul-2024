import os
import random
import shutil

# deterministic random seed
random.seed(2)

ScriptDir = os.path.dirname(os.path.realpath(__file__))
GalleryDir = os.path.join(ScriptDir, 'gallery')

def main():
    # 1. copy over the selected photos from the experience folder
    # 2. copy over the photos from the source folder, by randomizing the names of the files in a deterministic way

    # 1. copy over the selected photos from the experience folder
    experience_folder = os.path.join(ScriptDir, 'experience')
    for root, dirs, files in os.walk(experience_folder):
        for file in files:
            if file.endswith('.jpg'):
                file_path = os.path.join(root, file)
                shutil.copy(file_path, GalleryDir)

    # 2. copy over the photos from the source folder, by randomizing the names of the files in a deterministic way
    source_folder = os.path.join(ScriptDir, 'source')
    source_files = os.listdir(source_folder)
    random.shuffle(source_files)
    for i, file in enumerate(source_files):
        if file.endswith('.jpg'):
            file_path = os.path.join(source_folder, file)
            index = i + 7  # start from 7
            new_file_path = os.path.join(GalleryDir, f'{index:03d}.jpg')
            shutil.copy(file_path, new_file_path)

    pass

main()
