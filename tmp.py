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
  "[1:v]format=yuva420p, fade=t=in:st=2:d=0:alpha=1, fade=t=out:st=5:d=0:alpha=1, scale=1920:1080:force_original_aspect_ratio=decrease, pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img1_1]; \
   [0:v][img1_1]overlay=shortest=1" \
-c:v h264_nvenc /home/kyue/Downloads/prev/output_video.mp4


ffmpeg -i /home/kyue/Downloads/prev/11.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -filter_complex \
"[1:v]format=yuva420p, fade=t=in:st=1:d=1:alpha=1,fade=t=out:st=3:d=1:alpha=1[v2]; \
 [0:v][v2]overlay=1:0:enable='between(t,10,20)'[v]" \
-map "[v]" -map 0:a \
-c:v libx264 -c:a copy /home/kyue/Downloads/prev/output_video.mp4


ffmpeg -i /home/kyue/Downloads/prev/11.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -filter_complex \
"[1:v]fade=t=in:st=1:d=0:alpha=1,fade=t=out:st=4:d=0:alpha=1,format=yuva420p, scale=1920:1080:force_original_aspect_ratio=decrease[ov]; \
[0:v][ov]overlay=1:enable='between(t,1,5)'[v]" \
-map "[v]" -map 0:a -map 1:a? -c:v h264_nvenc -c:a copy /home/kyue/Downloads/prev/output_video.mp4



ffmpeg -i /home/kyue/Downloads/prev/11.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -filter_complex \
"[1:v]format=yuva420p[v2]; \
 [0:v][v2]overlay=1:0:enable='between(t,10,20)'[v]" \
-map "[v]" -map 0:a \
-c:v libx264 -c:a copy /home/kyue/Downloads/prev/output_video.mp4

ffmpeg -hwaccel cuda  -i /mnt/win-ssd/Users/93415/Videos/resources/tmp/closing1.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -filter_complex \
"[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2[v1_scaled]; \
[1:v]scale=1920:1080:force_original_aspect_ratio=decrease,setpts=PTS-STARTPTS[upper]; \
[v1_scaled][upper] overlay=enable='between(t,0.1, 1.44)+between(t,2.452,3.668)+between(t,12.03,13.183)+between(t,17.04,18.15)+between(t,20.758,28.032)'[out]" \
-map [out], \
-map 0:a -c:v libx264 -preset fast -crf 22 -c:a aac \
-strict experimental '/mnt/win-ssd/Users/93415/Videos/resources/output_video_based_on_sound.mp4'



ffmpeg -hwaccel cuda -i /mnt/win-ssd/Users/93415/Videos/resources/tmp/closing1.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -filter_complex \
"[0:v] scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2[v1_scaled]; \
[1:v]scale=1920:1080:force_original_aspect_ratio=decrease,setpts=PTS-STARTPTS [upper]; \
[v1_scaled][upper] overlay=enable='between(t,0.1, 1.44)+between(t,2.452,3.668)+between(t,12.03,13.183)+between(t,17.04,18.15)+between(t,20.758,28.032)'[out]" \
-map [out] -map 0:a -c:v libx264 -preset fast -crf 22 -c:a aac -strict experimental \
"/mnt/win-ssd/Users/93415/Videos/resources/output_video_based_on_sound.mp4"


ffmpeg -hwaccel cuda -i /mnt/win-ssd/Users/93415/Videos/resources/tmp/closing1.mp4 -i /mnt/win-ssd/Users/93415/Videos/resources/opening.mp4 -filter_complex \
"[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2[v1_scaled]; \
[1:v]scale=1920:1080:force_original_aspect_ratio=decrease,setpts=PTS-STARTPTS [upper]; \
[v1_scaled][upper]overlay=enable='between(t,0.0,1.44)+between(t,2.452,3.668)+between(t,12.03,13.183)+between(t,17.04,18.15)+between(t,20.758,28.032)'[out]" \
-c:v h264_nvenc -c:a copy /mnt/win-ssd/Users/93415/Videos/resources/output_video_based_on_sound.mp4


ffmpeg -hwaccel cuda -i /home/kyue/Desktop/ss.mp4 -i '/mnt/ssd/Pictures/YT_sources/2/_1_the AI revolution is speeding up/0.jpg' -filter_complex \
"[1:v]loop=loop=-1:size=1:start=0, format=yuva420p, fade=t=in:st=10:d=1:alpha=1,fade=t=out:st=13:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img2_1]; \
[0:v][img2_1] overlay=shortest=1"  \
-c:v h264_nvenc -c:a copy /home/kyue/Downloads/output_video.mp4


ffmpeg -hwaccel cuda -i /home/kyue/Desktop/ss10.mp4 -i '/mnt/ssd/Pictures/YT_sources/2/_1_the AI revolution is speeding up/0.jpg' \
-filter_complex "[1:v]loop=loop=-1:size=1:start=0, format=yuva420p, fade=t=in:st=12:d=1:alpha=1,fade=t=out:st=15:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black@0[img2_1]; \
[0:v][img2_1] overlay=shortest=1"  \
-c:v h264_nvenc -c:a copy /home/kyue/Desktop/output_video.mp4


ffmpeg -hwaccel cuda -i /home/kyue/Desktop/output_video.mp4 -i '/mnt/ssd/Pictures/YT_source_vd/1/_1_the AI revolution is speeding up/pexels-yaroslav-shuraev-8464662 (2160p).mp4' -i '/mnt/ssd/Pictures/YT_source_vd/1/_11_intentionally adding a lifespan to these AI programs/pexels-kindel-media-8566722 (Original).mp4' -i '/mnt/ssd/Pictures/YT_source_vd/1/_15_research indicating telomere lengths can predict lifespan/pexels-google-deepmind-18069473 (2160p).mp4' -i '/mnt/ssd/Pictures/YT_source_vd/1/_16_women generally outliving men due to longer telomere lengths/production_id_4873451 (1080p).mp4' -i '/mnt/ssd/Pictures/YT_source_vd/1/_17_women in the U.S. living about five to six years longer than men/pexels-tima-miroshnichenko-5813768 (2160p).mp4' -filter_complex \
"[1:v]format=yuva420p, fade=t=in:st=18:d=1:alpha=1,fade=t=out:st=25:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease [img2_1]; [2:v]format=yuva420p, fade=t=in:st=98:d=1:alpha=1,fade=t=out:st=105:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease [img12_1]; [3:v]format=yuva420p, fade=t=in:st=170:d=1:alpha=1,fade=t=out:st=177:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease [img16_1]; [4:v]format=yuva420p, fade=t=in:st=175:d=1:alpha=1,fade=t=out:st=182:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease [img17_1]; [5:v]format=yuva420p, fade=t=in:st=184:d=1:alpha=1,fade=t=out:st=191:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease [img18_1]; \
[0:v][img2_1] overlay=1:enable='between(t,10,18)' [tmp1];[tmp1][img12_1] overlay=1:enable='between(t,90,98)' [tmp2];[tmp2][img16_1] overlay=1:enable='between(t,162,170)' [tmp3];[tmp3][img17_1] overlay=1:enable='between(t,167,175)' [tmp4];[tmp4][img18_1] overlay=1:enable='between(t,176,184)'" \
-c:v h264_nvenc -c:a copy /home/kyue/Desktop/merge_vid.mp4

ffmpeg -hwaccel cuda -i /home/kyue/Desktop/output_video.mp4 -i '/mnt/ssd/Pictures/YT_source_vd/2/_1_the AI revolution is speeding up/pexels-yaroslav-shuraev-8464662 (2160p).mp4' -filter_complex \
"[1:v]format=yuva420p, fade=t=in:st=18:d=1:alpha=1,fade=t=out:st=25:d=1:alpha=1,scale=1920:1080:force_original_aspect_ratio=decrease [img2_1]; \
[0:v][img2_1] overlay=enable=gte(t\,5)[out]" \
-map [out] -map 0:a -c:v libx264 -preset fast -crf 22 -c:a aac -strict experimental \
"/home/kyue/Desktop/1.mp4"


ffmpeg -hwaccel cuda -i /home/kyue/Desktop/output_video.mp4 -i '/mnt/ssd/Pictures/YT_source_vd/2/_1_the AI revolution is speeding up/pexels-yaroslav-shuraev-8464662 (2160p).mp4' -filter_complex \
"[1:v]setpts=PTS-STARTPTS+10/TB[v2_delayed];[0:v][v2_delayed]overlay=enable='between(t,10,18)'[out]" \
-map "[out]" -map 0:a? -c:v libx264 -c:a copy \
"/home/kyue/Desktop/1.mp4"
