import moviepy.editor as moviepy
import os

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), '')

clip = moviepy.VideoFileClip(c+"3.avi")
clip.write_videofile(c+"3.mp4")