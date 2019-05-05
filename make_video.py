from bs4 import BeautifulSoup
import re
import requests
import cv2
from moviepy.editor import *

text = '''

'''
url_video = r'https://webinar.nocvko.ru/' +'



# def find_time_in_text(text):
#     soup = BeautifulSoup(text, features="html.parser")
#     result = []
#     print(soup.prettify())
#     for link in soup.find_all("span", "thumbnail-label"):
#         hms = re.split(r':', link.string)
#         second = int(hms[2]) + int(hms[1]) * 60 + int(hms[0]) * 3600
#         # print(second)
#         result.append(second)
#     return result
def find_time_in_text(text):
    soup = BeautifulSoup(text, features="html.parser")
    result = []
    # print(soup.prettify())
    for link in soup.find_all('img'):
        second = int(link.get('data-out'))
        # print(second)
        result.append(second)
    return result


def find_picture_in_text(text):
    soup = BeautifulSoup(text, features="html.parser")
    result = []
    # print(soup.prettify())
    for link in soup.find_all("img"):
        adr = 'https://webinar.nocvko.ru/' + link.get('src')
        # print(adr)
        result.append(adr)
    return result


def get_pictures(url_list):
    for i in range(len(url_list)):
        name = url_list[i]
        picture = requests.get(name)
        with open(str(i) + '.png', 'wb') as f:
            f.write(picture.content)

# def find_picture_in_text(text):
#     soup = BeautifulSoup(text, features="html.parser")
#     soup.find('video/webm')
def get_video(url):
    video = requests.get(url)
    with open('temp.webm', 'wb') as f:
        f.write(video.content)


def make_video(timing):
    # fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    wr = cv2.VideoWriter('temp_video.avi', fourcc, 1.0, (1600, 1200))
    prev_time = 0
    for slide_num in range(len(timing)):
    # for slide_num in range(5):
        print('Start slide', slide_num)
        slide = cv2.imread(str(slide_num) + '.png')
        for second in range(timing[slide_num] - prev_time):
            wr.write(slide)
        prev_time = timing[slide_num]
    wr.release()
    cv2.destroyAllWindows()


t = find_time_in_text(text)
# print(t)
a = find_picture_in_text(text)
get_pictures(a)
make_video(t)
print('скачивание видео из сети')
get_video(url_video)

audio_clip = AudioFileClip("temp.webm")
#     # audio_clip.write_audiofile("temp_audio.ogg", fps=48000, bitrate='96k', codec='libvorbis')
videoclip = VideoFileClip('temp_video.avi').subclip(0, audio_clip.duration)
#     # audio_clip = AudioFileClip("temp_audio.ogg")
videoclip.set_audio(audio_clip).write_videofile("7 Проектирование нового продукта.avi", codec='mpeg4')
