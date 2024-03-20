from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import subprocess
import os

# Function to detect non-silent parts of the audio
def detect_sound_segments(audio_path, min_silence_len=1000, silence_thresh=-40):
    sound = AudioSegment.from_file(audio_path)
    non_silent_parts = detect_nonsilent(sound, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
    
    # Finding the duration of the sound
    sound_duration = len(sound)

    # Detect silent parts by inverting non-silent parts
    silent_parts = []
    last_slice_end = 0
    for start, end in non_silent_parts:
        if last_slice_end < start:
            silent_parts.append((last_slice_end, start))
        last_slice_end = end
    if last_slice_end < sound_duration:
        silent_parts.append((last_slice_end, sound_duration))
    
    return silent_parts

# Function to run ffmpeg commands
def run_ffmpeg_command(cmd):
    subprocess.run(cmd, shell=True)



def craft_ffmpeg_cmd(v1_path, v2_path, time_ranges, output_path):
    # Prepare the enable expressions for overlay filter
    enable_expressions = ["between(t,{start},{end})".format(start=start/1000, end=end/1000) for start, end in (time_ranges)]
    enable_expression = '+'.join(enable_expressions)

    # FFmpeg command with dynamic overlay times
    cmd = [
        'ffmpeg',
        '-hwaccel', 'cuda',
        '-i', v1_path,  # Input file v1
        '-i', v2_path,  # Input file v2
        '-filter_complex',
        '-map', '[out]',  # Map the overlay output video
        '-map', '0:a',  # Map the audio from v1
        '-c:v', 'libx264',  # Video codec
        '-preset', 'fast',  # Encoding speed/quality trade-off
        '-crf', '22',  # Constant Rate Factor (quality level, lower is better)
        '-c:a', 'aac',  # Audio codec
        '-strict', 'experimental',
        output_path  # Output file
    ]

    overlay_filters = ["[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2[v1_scaled]," # Scale and pad v1
                       "[1:v]scale=1920:1080:force_original_aspect_ratio=decrease,setpts=PTS-STARTPTS[upper];",  # Scale and ensure v2 starts from 0
                       "[v1_scaled][upper]overlay=enable='{enable_expression}'[out]".format(enable_expression=enable_expression),  # Dynamic overlay conditions
                       ]
    
    overlay_cmd = "".join(overlay_filters)

    input_cmds = [f"-i {v1_path}", f"-i {v2_path}"]

    ffmpeg_cmd = (
        f"ffmpeg -hwaccel cuda {' '.join(input_cmds)} -filter_complex \"{''.join(overlay_cmd)}\" "
        f" -c:v h264_nvenc -map [out] -map 0:a -preset fast -crf 22 -c:a aac -strict experimental {output_path}"
    )

    

    return ffmpeg_cmd




# Extract audio from the primary video
primary_video_path = "/home/kyue/Desktop/_11_soul.mp4"
background_video_path = "/mnt/win-ssd/Users/youtube+pics/nowhand_drawing/scenarios/_1_flitering_vs_handinpocket/no_talking.mp4"


primary_video_path = "/home/kyue/Desktop/_12_soul.mp4"
scene = "_2_skpetical_vs_enthus/"

primary_video_path = "/home/kyue/Desktop/_13_soul.mp4"
scene = "_4_holo_holdpen_layonsofa/"

primary_video_path = "/home/kyue/Desktop/_22_sushi.mp4"
scene = "_5_raisefinger_vs_holdhair/"
scene = "_3_thumbup_reserved"



background_video_path = "/mnt/win-ssd/Users/youtube+pics/nowhand_drawing/scenarios/{:s}/no_talking.mp4".format(scene)

audio_extract_path = "/tmp/extracted_audio.mp3"
extract_audio_cmd = f"ffmpeg -i {primary_video_path} -q:a 0 -map a {audio_extract_path}"
output_path = "/home/kyue/Desktop/out.mp4"
run_ffmpeg_command(extract_audio_cmd)

# Detect sound segments in the extracted audio
sound_segments = detect_sound_segments(audio_extract_path)
print(sound_segments)

ffmpeg_cmd = craft_ffmpeg_cmd(primary_video_path, background_video_path, sound_segments, output_path)

print("-"*80)
print("".join(ffmpeg_cmd))

run_ffmpeg_command(ffmpeg_cmd)
