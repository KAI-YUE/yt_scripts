from moviepy.editor import VideoFileClip

def convert_to_wav(input_file, output_file):
    # Load the video clip
    video = VideoFileClip(input_file)

    # Extract the audio from the video clip
    audio = video.audio

    # Write the audio to a WAV file
    audio.write_audiofile(output_file, codec='pcm_s16le')

    print("Conversion completed successfully!")

# Usage example
# input_file = "/home/kyue/Downloads/22.mp4"
# input_file = "/home/kyue/Downloads/11.mp4"
input_file = "/mnt/win-ssd/Users/93415/Videos/_1_eden_.mp4"

# WAV file
output_file = "/home/kyue/Audio/_1_eden_.wav"
convert_to_wav(input_file, output_file)
