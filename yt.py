import pytube

#Enter the Youtube URL
url = input('Enter the Youtube URL: ')

#Access the video
youtube = pytube.YouTube(url)

#Get the video title
title = youtube.title

#Get the video streams
video_streams = youtube.streams.all()

#Choose the video quality
for stream in video_streams:
    print(f'{stream}')

choice = int(input('Enter the number of the video quality you want to download: '))

#Download the video
selected_stream = video_streams[choice-1]
selected_stream.download('downloads/')

print(f'{title} has been downloaded successfully!')