ffmpeg -hwaccel cuda -i video.mp4 -i overlay.png -filter_complex \
"[1:v]format=yuva420p,fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=3:d=1:alpha=1[ov]; \
 [0:v][ov]overlay=W-w-10:H-h-10:shortest=1" \
-c:v h264_nvenc -preset fast output_video.mp4


ffmpeg -hwaccel cuda -i 11.mp4 -i /home/kyue/Pictures/tmp/faces/1.png -filter_complex \
"[1:v]format=yuva420p,pad=W:H:(ow-iw)/2:(oh-ih)/2:color=black@0,fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=3:d=1:alpha=1[ov]; \
 [0:v][ov]overlay=shortest=1" \
-c:v h264_nvenc -preset fast output_video.mp4

ffmpeg -hwaccel cuda -i 11.mp4 -i /home/kyue/Pictures/Wallpapers/1.jpg -filter_complex \
"[1:v]format=yuva420p,fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=3:d=1:alpha=1, \
 scale=1920:1080:force_original_aspect_ratio=decrease, \
 pad='iw+mod(iw,2)':'ih+mod(ih,2)':(ow-iw)/2:(oh-ih)/2:color=black@0[ov]; \
 [0:v][ov]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1" \
-c:v h264_nvenc -preset fast output_video.mp4


ffmpeg -hwaccel cuda -i 11.mp4 -i /home/kyue/Pictures/Wallpapers/1.jpg -filter_complex \
"[1:v]format=yuva420p,fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=3:d=1:alpha=1, \
 scale=1920:1080:force_original_aspect_ratio=decrease, \
 pad='iw+mod(iw,2)':'ih+mod(ih,2)':(ow-iw)/2:(oh-ih)/2:color=black@0[ov]; \
 [0:v][ov]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1" \
-c:v h264_nvenc -preset fast output_video.mp4


ffmpeg -hwaccel cuda -i 11.mp4 -i /home/kyue/Pictures/Wallpapers/1.jpg -filter_complex \
"[1:v]scale=1920:1080,format=yuva420p,fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=3:d=1:alpha=1[img]; \
[0:v][img]overlay=0:0:shortest=1" -c:v libx264 output_video.mp4

ffmpeg -hwaccel cuda -i 11.mp4 -i /home/kyue/Pictures/Wallpapers/1.jpg -filter_complex \
"[1:v]format=yuva420p,fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=3:d=1:alpha=1, \
scale=1920:1080:force_original_aspect_ratio=decrease, \
pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img]; \
[0:v][img]overlay=0:0:shortest=1" \
-c:v libx264 output_video.mp4

ffmpeg -hwaccel cuda -i 11.mp4 -i /home/kyue/Pictures/Wallpapers/1.jpg -filter_complex \
"[1:v]format=yuva420p,fade=t=in:st=1:d=1:alpha=1,\
scale=1920:1080:force_original_aspect_ratio=decrease,\
pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img];\
[0:v][img]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2" \
-c:v libx264 output_video.mp4




ffmpeg -hwaccel cuda -i /home/kyue/Downloads/11.mp4 -i /home/kyue/Pictures/Wallpapers/1.jpg -filter_complex \
"[1:v]loop=loop=-1:size=1:start=0,format=yuva420p,fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=2:d=1:alpha=1,\
scale=1920:1080:force_original_aspect_ratio=decrease,\
pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img];\
[0:v][img]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1" \
-i /home/kyue/Pictures/Wallpapers/1.jpg -filter_complex \
"[1:v]loop=loop=-1:size=1:start=0,format=yuva420p,fade=t=in:st=1:d=6:alpha=1,fade=t=out:st=7:d=1:alpha=1,\
scale=1920:1080:force_original_aspect_ratio=decrease,\
pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img];\
[0:v][img]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1" \
-c:v h264_nvenc output_video.mp4

loop=loop=-1:size=1:start=0,

ffmpeg -hwaccel cuda -i /home/kyue/Downloads/11.mp4 -i /home/kyue/Pictures/Wallpapers/1.jpg -i /home/kyue/Pictures/Wallpapers/1.jpg -filter_complex \
"[1:v]loop=loop=-1:size=1:start=0, format=yuva420p,fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=2:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1]; \
[1:v]loop=loop=-1:size=1:start=0, format=yuva420p,fade=t=in:st=3:d=1:alpha=1,fade=t=out:st=4:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img2]; \
[0:v][img1]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1[tmp1]; \
[tmp1][img2]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1" \
-c:v h264_nvenc output_video.mp4

ffmpeg -hwaccel cuda -i /home/kyue/Downloads/11.mp4 -i '/mnt/ssd/Pictures/YT_sources/2/_0_AI technology is advancing/0.jpg' -i '/mnt/ssd/Pictures/YT_sources/2/_0_AI technology is advancing/1.jpg' -filter_complex \
"[1:v]loop=loop=-1:size=1:start=0, format=yuva420p,fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=12:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_1]; \
[2:v]loop=loop=-1:size=1:start=0, format=yuva420p,fade=t=in:st=14:d=1:alpha=1,fade=t=out:st=12:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_2]; \
[0:v][img1_1]overlay=shortest=1 [tmp1]; \
[tmp1][img1_2]overlay=shortest=1 " \
-c:v h264_nvenc /home/kyue/Downloads/output_video.mp4


ffmpeg -hwaccel cuda -i /home/kyue/Downloads/out0240.mp4 -i '/mnt/ssd/Pictures/YT_sources/2/_0_AI technology is advancing/0.jpg' -i '/mnt/ssd/Pictures/YT_sources/2/_0_AI technology is advancing/1.jpg' -filter_complex \
"[1:v]loop=loop=-1:size=1:start=0, format=yuva420p,fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=12:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_1]; \
[2:v]loop=loop=-1:size=1:start=0, format=yuva420p,fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=12:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_2]; \ 
[0:v][img1_1]overlay=shortest=1 [tmp1]; \
[0:v][img1_2]overlay=shortest=1 " 
-c:v h264_nvenc /home/kyue/Downloads/output_video.mp4

ffmpeg -hwaccel cuda -i /home/kyue/Downloads/out0240.mp4 -i '/mnt/ssd/Pictures/YT_sources/2/_0_AI technology is advancing/0.jpg' -i '/mnt/ssd/Pictures/YT_sources/2/_0_AI technology is advancing/1.jpg' -filter_complex  \ 
"[1:v]loop=loop=-1:size=1:start=0, format=yuva420p,fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=12:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_1]; \
[2:v]loop=loop=-1:size=1:start=0, format=yuva420p,fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=12:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_2]; \ 
[tmp0][img1_1]overlay=shortest=1 [tmp1]; 
[tmp0][img1_2]overlay=shortest=1 [tmp1]" -c:v h264_nvenc /home/kyue/Downloads/output_video.mp4


ffmpeg -hwaccel cuda -i /home/kyue/Downloads/out0240.mp4 -i '/mnt/ssd/Pictures/YT_sources/2/_0_AI technology is advancing/0.jpg' -i '/mnt/ssd/Pictures/YT_sources/2/_0_AI technology is advancing/1.jpg' -filter_complex \ 
"[1:v]loop=loop=-1:size=1:start=0, format=yuva420p, fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=12:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_1]; \
[2:v]loop=loop=-1:size=1:start=0, format=yuva420p, fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=12:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_2]; \ 
[0:v][img1_1] overlay=shortest=1 [tmp1]; \
[tmp1][img1_2] overlay=shortest=1 [tmp2]; " 
-c:v h264_nvenc /home/kyue/Downloads/output_video.mp4

ffmpeg -hwaccel cuda -i /home/kyue/Downloads/out0240.mp4 -i /home/kyue/Pictures/Wallpapers/1.jpg -i /home/kyue/Pictures/Wallpapers/1.jpg -filter_complex \
"[1:v]loop=loop=-1:size=1:start=0, format=yuva420p, fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=12:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_1]; \
[2:v]loop=loop=-1:size=1:start=0, format=yuva420p, fade=t=in:st=9:d=1:alpha=1,fade=t=out:st=13:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_2]; \
[0:v][img1_1] overlay=shortest=1 [tmp1]; \
[tmp1][img1_2] overlay=shortest=1" \
-c:v h264_nvenc /home/kyue/Downloads/output_video.mp4



ffmpeg -hwaccel cuda -i /home/kyue/Downloads/prev/11.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -filter_complex \
"[1:v]format=yuva420p,fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=2:d=1:alpha=1,\
scale=1920:1080:force_original_aspect_ratio=decrease,\
pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[overlay]; \
[0:v][overlay]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1" \
-c:v h264_nvenc /home/kyue/Downloads/prev/output_video.mp4

ffmpeg -hwaccel cuda -i /mnt/win-ssd/Users/93415/Videos/resources/closing_final.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -filter_complex \
"[1:v]format=yuva420p, fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=11:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_1]; \
[2:v]format=yuva420p, fade=t=in:st=12:d=1:alpha=1,fade=t=out:st=15:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img2_1]; \
[0:v][img1_1] overlay=shortest=1 [tmp1]; \
[tmp1][img2_1] overlay=shortest=1"  \
-c:v h264_nvenc /home/kyue/Downloads/prev/output_video.mp4



ffmpeg -hwaccel cuda -i /home/kyue/Downloads/prev/out0240.mp4 -i '/mnt/win-ssd/Users/93415/Videos/resources/opening.mp4' -filter_complex \
"[1:v]format=yuva420p, fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=11:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease[img1_1]; \
[0:v][img1_1] overlay=shortest=1" \
-c:v h264_nvenc /home/kyue/Downloads/prev/output_video.mp4


ffmpeg -hwaccel cuda \
  -i /mnt/win-ssd/Users/93415/Videos/resources/closing_final.mp4 \
  -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 \
  -filter_complex \
  "[1:v]format=yuva420p, fade=t=in:st=2:d=1:alpha=1, fade=t=out:st=5:d=1:alpha=1, scale=1920:1080:force_original_aspect_ratio=decrease, pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_1]; \
   [0:v][img1_1]overlay=shortest=1" \
-c:v h264_nvenc /home/kyue/Downloads/prev/output_video.mp4


ffmpeg -i /home/kyue/Downloads/prev/11.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -filter_complex \
"[1:v]format=yuva420p, fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=3:d=1:alpha=1[v2]; \
 [0:v][v2]overlay=1:0:enable='between(t,10,20)'[v]" \
-map "[v]" -map 0:a \
-c:v libx264 -c:a copy /home/kyue/Downloads/prev/output_video.mp4


ffmpeg -i /home/kyue/Downloads/prev/11.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -filter_complex \
"[1:v]fade=t=in:st=0:d=1:alpha=1,fade=t=out:st=4:d=1:alpha=1,format=yuva420p, scale=1920:1080:force_original_aspect_ratio=decrease[ov]; \
[0:v][ov]overlay=1:enable='between(t,1,5)'[v]" \
-map "[v]" -map 0:a -map 1:a? -c:v libx264 -c:a copy /home/kyue/Downloads/prev/output_video.mp4


'ffmpeg -hwaccel cuda -i /home/kyue/Downloads/prev/out0240.mp4 -i '/mnt/ssd/Pictures/YT_source_vd/2/_0_AI technology is advancing/pexels-jack-sparrow-5977261 (2160p).mp4' -i '/mnt/ssd/Pictures/YT_source_vd/2/_0_Solar Project can automatically convert text into video/production_id_5092425 (1080p).mp4' -filter_complex \
"[1:v]format=yuva420p, fade=t=in:st=8:d=1:alpha=1,fade=t=out:st=11:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease; \
[2:v]format=yuva420p, fade=t=in:st=10:d=1:alpha=1,fade=t=out:st=13:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease; \
[0:v][img1_1] overlay=1:enable='between(t,8,12)' [tmp1]; \
[tmp1][img2_1] overlay=1:enable='between(t,10,14)'"  \
-c:v h264_nvenc -c:a copy /home/kyue/Downloads/prev/output_video.mp4'