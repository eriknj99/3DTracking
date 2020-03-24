ffmpeg -r 30 -f image2 -s 512x512 -i set0/X/%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p set0/X/x.mp4
ffmpeg -r 30 -f image2 -s 512x512 -i set0/Y/%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p set0/Y/y.mp4
ffmpeg -r 30 -f image2 -s 512x512 -i set0/Z/%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p set0/Z/z.mp4
