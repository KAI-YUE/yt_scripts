import subprocess

# Define the paths to your video files
v1_path = "/mnt/win-ssd/Users/93415/Videos/resources/tmp/closing1.mp4"
v2_path = "/mnt/win-ssd/Users/93415/Videos/resources/opening.mp4"
output_path = '/mnt/win-ssd/Users/93415/Videos/resources/output.mp4'

# FFmpeg command
cmd = [
    'ffmpeg',
    '-i', v1_path,  # Input file v1
    '-i', v2_path,  # Input file v2
    '-filter_complex',
    "[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2[v1_scaled];"  # Scale and pad v1
    "[1:v]scale=1920:1080:force_original_aspect_ratio=decrease,setpts=PTS-STARTPTS[upper];"  # Scale and ensure v2 starts from 0
    "[v1_scaled][upper]overlay=enable='between(t,1,2)+between(t,5,6)'[out]",  # Overlay conditions
    '-map', '[out]',  # Map the overlay output video
    '-map', '0:a',  # Map the audio from v1
    '-c:v', 'libx264',  # Video codec
    '-preset', 'fast',  # Encoding speed/quality trade-off
    '-crf', '22',  # Constant Rate Factor (quality level, lower is better)
    '-c:a', 'aac',  # Audio codec
    '-strict', 'experimental', 
    output_path  # Output file
]

# Run the FFmpeg command
subprocess.run(cmd)