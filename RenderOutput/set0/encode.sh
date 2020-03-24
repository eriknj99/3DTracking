ffmpeg -r 30 -f image2 -s 512x512 -i X/%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p X/x.mp4
ffmpeg -r 30 -f image2 -s 512x512 -i Y/%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p Y/y.mp4
ffmpeg -r 30 -f image2 -s 512x512 -i Z/%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p Z/z.mp4
