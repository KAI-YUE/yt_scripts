import re

def clean_subtitles(subtitle_text):
    # Remove timestamps and line numbers
    cleaned_text = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n', '', subtitle_text)

    # Split the text into lines
    lines = cleaned_text.split('\n')

    # De-duplicate the lines (keeping only even-indexed lines which are in Traditional Chinese)
    deduplicated_lines = [line for index, line in enumerate(lines) if index % 2 != 0]

    # Join the lines back into a single string and remove extra newlines
    deduplicated_text = '\n'.join(deduplicated_lines)
    deduplicated_text = re.sub(r'\n\s*\n', '\n', deduplicated_text)

    return deduplicated_text

# Example usage
# subtitle_text = """
# 322
# 00:10:42,420 --> 00:10:44,900
# 至少应该知道这些东西的背后
# 至少應該知道這些東西的背後

# 323
# 00:10:44,910 --> 00:10:48,760
# 他体现的都是美国AI技术的强大的实力
# 他體現的都是美國AI技術的強大的實力
# """

file_path = "/mnt/win-ssd/Users/93415/Downloads/sora.srt"
with open(file_path, 'r', encoding='utf-8') as file:
    subtitle_text = file.read()

cleaned_text = clean_subtitles(subtitle_text)
print(cleaned_text)

with open('/mnt/win-ssd/Users/93415/Downloads/cleaned_subtitle.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)
