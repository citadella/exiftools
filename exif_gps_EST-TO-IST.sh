#!/bin/bash

# Target directory
target_dir="/path/to/files"

# Function to add 4.5 hours to Exif photo taken time
add_hours_to_exif() {
    local file="$1"
    exiftool "-DateTimeOriginal+=0:0:0 4:30:0" "$file"
}

# Iterate through JPG files in the target directory
for jpg_file in "$target_dir"/*.JPG; do
    add_hours_to_exif "$jpg_file"
    echo "Added 4.5 hours to Exif photo taken time for $jpg_file"
done
