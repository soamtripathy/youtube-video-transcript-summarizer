from flask import Flask, request, render_template
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/summary', methods=['POST'])
def summary_api():
    url = request.form["url"]
    video_id = url.split('=')[-1]
    transcript = get_transcript(video_id)
    summary = get_summary(transcript)
    length_transcript = len(transcript)
    summary_length = len(summary)
    return render_template("index.html", transcript=transcript, summary=summary, length_transcript=length_transcript, summary_length=summary_length)


def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript


def get_summary(transcript):
    summariser = pipeline('summarization')
    summary = ''
    for i in range(0, (len(transcript)//1000)+1):
        summary_text = summariser(
            transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary = summary + summary_text + ' '
    return summary


if __name__ == '__main__':
    app.run(port=8000)
