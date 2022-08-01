import os
import hashlib
import requests
from moviepy.editor import VideoFileClip

# There is string s = "Python Bootcamp". Write the code that hashes string.

s = 'Python Bootcamp'


def hash_function(value):
    return hashlib.sha1(value.encode('utf-8')).hexdigest()


# You are working on a project for TikTok. The future project will be a web-site of all public GIF images.
# You need to write a function that converts TikTok video to GIF.
# The input parameter is url address of TikTok video, i.e. "TikTok example".
# The output parameter is path to GIF image, i.e. "/home/user/TikTok-example-1.gif".


def converter(url):
    r = requests.get(url, stream=True)

    with open('video', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)

    clip = VideoFileClip("video")
    clip = clip.subclip(0, 3)
    clip.write_gif("gif_gif.gif")

    return os.path.abspath('gif_gif.gif')


if __name__ == "__main__":
    print(hash_function(s))
    print(converter(input()))
