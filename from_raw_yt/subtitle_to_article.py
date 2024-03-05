import re

def clean_subtitles(subtitle_text):
    # Remove timestamps and line numbers
    cleaned_text = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n', '', subtitle_text)

    # Remove any additional empty lines
    cleaned_text = re.sub(r'\n\s*\n', '', cleaned_text)

    return cleaned_text

def read_and_clean_srt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        subtitle_text = file.read()
        return clean_subtitles(subtitle_text)

# Example usage
file_path = "/mnt/win-ssd/Users/93415/Downloads/his.srt"
cleaned_text = read_and_clean_srt_file(file_path)

with open('/mnt/win-ssd/Users/93415/Downloads/cleaned_subtitle.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)


