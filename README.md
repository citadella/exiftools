# exiftools
Tools for editing exif data of photos

adjacent_exif_GPS_copy.py 
Runs through all files in a folder checking first if it has GPS exif data and then, if not, checking for other files in the directory and, if they have DateTimeOriginal timestamps of within 5 minutes, applying the same GPS data
In this case it uses .jpg files as the check source and .heic files to pull from, based on the fact that my Fuji camera saves in .jpg but often doesn't have GPS data and my iPhone files also upload to the same directory but always do, so it copies GPS data from the iPhone photo to the Fuji ones
