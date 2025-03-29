from flask import Flask, render_template, send_file
from pytubefix import YouTube

app = Flask(__name__ , static_folder='static')

def getAudio(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    path = audio_stream.download(output_path='./audio')
    return path

def getMpFour(link):
    
    yt = YouTube(link)
    
    video = yt.streams.get_highest_resolution()
    filePath = video.download('./video')
    return filePath

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/video/<path:url>')
def video(url):
    video = getMpFour(url)
    return send_file(video)

@app.route('/audio/<path:url>')
def audio(url):
    audio = getAudio(url)
    return send_file(audio)

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(debug=True)