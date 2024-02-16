import os
from datetime import datetime, timedelta
from subprocess import check_output, run

target_dir = input("Enter the directory path: ")

# Validate the directory
if not os.path.exists(target_dir):
    print("Error: Directory does not exist.")
    exit()

for jpg_file in os.listdir(target_dir):
    if jpg_file.lower().endswith(".jpg"):
        jpg_path = os.path.join(target_dir, jpg_file)
        print(f"{datetime.now().strftime('%F %T')} - Processing file: {jpg_path}")

        # Check if the JPG file already has GPS data
        gps_check_output = check_output(["exiftool", "-gpslatitude", "-gpslongitude", jpg_path])
        if b"GPS Latitude" in gps_check_output and b"GPS Longitude" in gps_check_output:
            print("GPS data already exists. Skipping.")
            continue

        # Extract DateTimeOriginal value from the JPG file
        jpg_datetime_output = check_output(["exiftool", "-s3", "-d", "%Y:%m:%d %H:%M:%S", "-DateTimeOriginal", jpg_path])
        jpg_datetime = jpg_datetime_output.decode("utf-8").strip()

        # Check if jpg_datetime is empty
        if not jpg_datetime:
            print(f"Error: DateTimeOriginal value is empty for {jpg_path}. Skipping.")
            continue

        print(f"DateTimeOriginal value for {jpg_path}: {jpg_datetime}")

        heic_file = None
        for heic_filename in os.listdir(target_dir):
            if heic_filename.lower().endswith(".heic"):
                heic_path = os.path.join(target_dir, heic_filename)
                heic_datetime_output = check_output(["exiftool", "-s3", "-d", "%Y:%m:%d %H:%M:%S", "-DateTimeOriginal", heic_path])
                heic_datetime = heic_datetime_output.decode("utf-8").strip()

                # Check if heic_datetime is empty
                if not heic_datetime:
                    print(f"Error: DateTimeOriginal value is empty for {heic_path}. Skipping.")
                    continue

                time_diff = (datetime.strptime(jpg_datetime, "%Y:%m:%d %H:%M:%S") - datetime.strptime(heic_datetime, "%Y:%m:%d %H:%M:%S")).total_seconds() / 60

                if abs(time_diff) <= 5:
                    heic_file = heic_path
                    break

        if heic_file:
            heic_filename = os.path.basename(heic_file)
            run(["exiftool", "-tagsfromfile", heic_file, "-gps:all", "-overwrite_original", jpg_path])
            print(f"GPS coordinates copied successfully from {heic_filename}.")
        else:
            print(f"No matching HEIC file found within 5 minutes for {jpg_path}.")
