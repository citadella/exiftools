#!/bin/bash

# Target directory
target_dir="/mnt/user/media/photos/2024/02/Test"

# Iterate through all files in the target directory
for file in "$target_dir"/*; do
    # Print the file name and its Exif photo taken time
    exiftool -DateTimeOriginal "$file" | grep "Date/Time Original" | sed "s/Date\/Time Original\s*:\s*//"
done
