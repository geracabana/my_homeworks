import os
import shutil
import datetime
import argparse
import PIL.Image 

parser = argparse.ArgumentParser()   
parser.add_argument('input_dir_photo', help='After the name of the program write the path down for the directory with the pictures')
parser.add_argument('output_dir_photo', help='After the directory with the pictures write the path down for the destination directory')
parser.add_argument('-d', '--delete', help='With this option you can delete the original directory wiht pictures')

args = parser.parse_args()
directin = args.input_dir_photo
directout = args.output_dir_photo 

def photosort(directin, directout):
    files_by_year = {}
    
    for filename in os.listdir(directin):
        if filename.endswith(".jpeg"):
            try:
                img = PIL.Image.open("img.jpg")
                exif_data = img._getexif()
                taken_date = datetime.datetime.strptime(exif_data['DateTimeOriginal'], 'y')
                year = taken_date.year
            except (AttributeError, KeyError):

                year = "unknown"

            if year not in files_by_year:
                files_by_year[year] = []
         
            files_by_year[year].append(filename)
    
  
    os.makedirs(directout, exist_ok=True)
    
  
    for year, filenames in files_by_year.items():
  
        year_dir = f"{directout}/{year}"
        os.makedirs(year_dir, exist_ok=True)
 
        sequence = 1
        for filename in filenames:
          
            try:
                img = PIL.Image.open('img.jpg')
                exif_data = img._getexif()
                taken_date = datetime.datetime.strptime(exif_data['DateTimeOriginal'], 'y')
                new_filename = f"{year}-{taken_date.month}-{taken_date.day}-{sequence}.jpg"
            except (AttributeError, KeyError):
                new_filename = f"{year}-{sequence}.jpg"
            shutil.move(f"{directin}/{filename}", f"{year_dir}/{new_filename}")
            sequence += 1
            
remove_original = args.delete     

if remove_original:
    response = input("Remove original photos? [y/N] ")
    if response.lower() == "y":
        photosort(directin, directout)
        os.rmdir(directin)
    elif response.upper() == "N":
        photosort(directin, directout)
    else:
        print('Okay, rewrite the input and output directories')