import os
import re
import subprocess

index = 32

# Path to the parent folder containing subfolders
parent_folder = "/mnt/ssd/Pictures/YT_source_vd/{:d}/".format(index)
# Path to the text file with timings
timings_file_path = '/home/kyue/Projects/YT/audio_transcription/keyword.txt'
# Path to the base video
base_video_path = "/home/kyue/Desktop/_{:d}_.mp4".format(index)
# Output video path
output_video_path = "/home/kyue/Desktop/merge_vid.mp4"


ref_img_folder = "/mnt/ssd/Pictures/YT_sources/{:d}/".format(index)


# Other parts of the script remain the same

# Execute the FFmpeg command
def execute_ffmpeg_cmd(ffmpeg_cmd):
    try:
        subprocess.run(ffmpeg_cmd, shell=True, check=True)
        print("FFmpeg command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute FFmpeg command: {e}")

# Function to parse timings from the text file
def parse_timings(filepath):
    timings = []
    with open(filepath, 'r') as file:
        for line in file:
            match = re.search(r'(.+), \((\d+):(\d+)\)', line)
            if match:
                description = match.group(1).strip()
                minutes = int(match.group(2))
                seconds = int(match.group(3))
                total_seconds = minutes * 60 + seconds
                timings.append((description, total_seconds))
    return timings

# Function to list all images in subfolders and process folder names
def list_images_in_subfolders(parent_folder):
    images = {}
    for root, dirs, files in os.walk(parent_folder):
        for file in files:
            if file.lower().endswith(('.mp4')):
                folder_name = os.path.basename(root)
                # Remove _%d_ prefix from folder name
                processed_folder_name = re.sub(r'^_\d+_', '', folder_name)
                if processed_folder_name not in images:
                    images[processed_folder_name] = []
                images[processed_folder_name].append(os.path.join(root, file))
    return images

# Constructing the FFmpeg command
# Function to construct the FFmpeg command
def construct_ffmpeg_cmd(base_video, images, timings, output_path):
    input_cmds = [f"-i {base_video}"]
    filter_complex_cmds = []
    overlay_filters = []

    counter = 0
    # Incremental offset in seconds for images within the same category
    incremental_offset = 1  # Adjust as needed to control the display duration of each image

    for idx, (desc, start_time) in enumerate(timings, start=1):
        if desc in images:
            # Reset incremental time for each new category
            incremental_time = start_time
            
            for img_idx, img_path in enumerate(images[desc], start=1):
                input_cmds.append(f"-i '{img_path}'")
                input_index = len(input_cmds) - 1  # Adjust for zero-based index
                duration = 8  # Default duration for each image
                fade_duration = 1  # Default fade duration
                
                # Find the last occurrence of '/' and keep everything before it
                path_without_filename = img_path.rsplit('/', 1)[0]

                # Step 2: Replace 'YT_source_vd' with 'YT_sources'
                updated_path = path_without_filename.replace("YT_source_vd", "YT_sources")

                # Count the number of files under the updated path
                file_count = 0
                for root, dirs, files in os.walk(updated_path):
                    file_count += len(files)

                # depends on the number of image files in the folder, we will add an delay
                delay = 3 + file_count*5

                # incremental_time = 0

                # Use incremental_time for fade in/out instead of start_time
                filter_complex_cmds.append(
                    f"[{input_index}:v] setpts=PTS-STARTPTS+{incremental_time+delay}/TB, format=yuva420p, fade=t=in:st={incremental_time+delay}:d={fade_duration}:alpha=1,"
                    f"fade=t=out:st={incremental_time + duration - fade_duration + delay}:d={fade_duration}:alpha=1,"
                    f"scale=1920:1080:force_original_aspect_ratio=decrease [img{idx}_{img_idx}];"
                    # f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img{idx}_{img_idx}];"
                )
                overlay_filters.append(
                    f"[tmp{counter}][img{idx}_{img_idx}] overlay=enable=gte(t\,3) [tmp{counter+1}];"
                )
                
                # Increment the time for the next image
                incremental_time += incremental_offset
                counter += 1
    
    # Final overlay command uses the last tmp variable, so we remove the last "[tmpX]" from the command
    # final_overlay_cmd = "".join(overlay_filters).replace("[tmp0][img1_1]", "[0:v][img1_1]").rstrip(f"; [tmp{counter}]")
    final_overlay_cmd = "".join(overlay_filters).replace("[tmp0]", "[0:v]")
    final_overlay_cmd = final_overlay_cmd[:-8]
    final_overlay_cmd += f"[out]"

    ffmpeg_cmd = (
        f"ffmpeg -hwaccel cuda {' '.join(input_cmds)} -filter_complex \"{' '.join(filter_complex_cmds + [final_overlay_cmd])}\" "
        f" -c:v h264_nvenc -map [out] -map 0:a -preset fast -crf 22 -c:a aac -strict experimental {output_path}"
    )
    
    return ffmpeg_cmd

# Main process
if __name__ == "__main__":
    timings = parse_timings(timings_file_path)
    images = list_images_in_subfolders(parent_folder)
    ffmpeg_cmd = construct_ffmpeg_cmd(base_video_path, images, timings, output_video_path)
    print(ffmpeg_cmd)

    # Execute the FFmpeg command
    execute_ffmpeg_cmd(ffmpeg_cmd)