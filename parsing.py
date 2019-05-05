import bs4
import os
import re
import os.path
from bs4 import BeautifulSoup


class Slide(object):
    from bs4 import BeautifulSoup

    def __init__(self, id_name='', link='', start=0.0, stop=0.0, width=1600, height=1200 ):
        self.id_name = id_name
        self.link = link
        self.start = start
        self.stop = stop
        self.width = width
        self.height = height

    @classmethod
    def from_tag_init(cls, image_tag):
        soup1 = BeautifulSoup(image_tag, "html.parser").image
        temp = cls(soup1['id'], soup1['xlink:href'], float(soup1['in']), float(soup1['out']), int(soup1['width']), int(soup1['height']))
        return temp

    def __str__(self):
        out = [self.id_name, self.link, self.start, self.stop, self.width, self.height]
        return str(out)






file_name = 'Recording Playback.html'
with open(file_name, 'r',encoding='UTF-8') as f:
    strings_list = f.readlines()
html_text = ''.join(strings_list)
soup = BeautifulSoup(html_text, 'html.parser')
parent_link = r'https://webinar.nocvko.ru/'

tag_list = soup.find(role="img").find_all('image')
slides = []
for tag in tag_list:
    slide = Slide.from_tag_init(str(tag))
    slides.append(slide)
# parent_link = soup.find('div', id='navbar').a['href']


video_link = soup.find(id='video').find('source', type='video/webm; codecs="vp8.0, vorbis"')['src']

print(parent_link + video_link)
for slide in slides:
    print(parent_link + slide.link)
print(os.system(r'cd ffmpeg/bin && ffmpeg.exe'))


# text = BeautifulSoup(html)
# for i in html:
#     print(i, end='')
# print(html)