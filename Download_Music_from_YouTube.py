from pytube import YouTube


# 進度條
def progress(chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%\n' %
          ('█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')
    print('下載完畢!')


if __name__ == '__main__':
    Youtube_url = input('請輸入網址:')
    yt = YouTube(Youtube_url, on_progress_callback=progress)
    video = yt.streams.filter(only_audio=True).first()
    video.download()
