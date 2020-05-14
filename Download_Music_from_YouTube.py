import os
from pytube import YouTube
import pytube
import easygui
from moviepy.editor import *


#進度條
def progress(chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % 
    ('█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')


Youtube_url =input('請輸入網址:')
yt = YouTube(Youtube_url, on_progress_callback=progress)
video =yt.streams.filter(only_audio=True).first()
video.download()
print('下載完畢!\n')

print('請選擇剛才下載完的MP4檔!')
Video_url = easygui.fileopenbox() #選擇Video檔案路徑
FileName=Video_url.split('\\') #字串切割
Music_Name=FileName[-1] #音樂檔名
Music_Name=Music_Name.split('.') #字串切割

#更改檔名
Old_name = str(Music_Name[0])+'.mp4'
New_name = str(Music_Name[0])+'.mp3'
os.rename(Old_name, New_name)
print('操作完畢!\n')