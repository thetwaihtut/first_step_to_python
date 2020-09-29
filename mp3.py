import moviepy.editor
video=moviepy.editor.VideoFileClip("/home/qwer/Videos/vokoscreenNG-2020-09-23_19-39-55.mp4")
audio=video.audio
audio.write_audiofile('first.mp3')
print('coverted successfully')
