import glob
from pydub import AudioSegment

def combine_audio_files(folder_path, output_filename):
    # Search for m4a files in the folder
    file_list = glob.glob(f"{folder_path}/*.m4a")
    file_list.sort()  # Sort files to maintain order

    # Initialize an empty audio segment
    combined = AudioSegment.empty()

    # Loop through the list and append each audio file
    for file in file_list:
        audio = AudioSegment.from_file(file, format="m4a")
        combined += audio

    # Export the combined audio as an MP3 file
    combined.export(output_filename, format="mp3")

folder_path = '/mnt/win-ssd/Users/93415/Downloads/m4a/'  # Replace with your folder path
output_filename = '/mnt/win-ssd/Users/93415/Downloads/mp3/output.mp3'  # Output file name

combine_audio_files(folder_path, output_filename)
