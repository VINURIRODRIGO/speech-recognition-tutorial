from api_communication import save_transcript  # pip install --user api
from yt_extractor import *
import json


def save_video_sentiments(url):
    video_infos = get_video_info(url)
    audio_url = get_audio_url(video_infos)
    if url:
        title = video_infos['title']
        title = title.strip().replace(" ", "_")
        title = title.strip().replace(":", "")
        title = "data/"+title
        save_transcript(audio_url, title, sentiment_analysis=True)


if __name__ == "__main__":
    # save_video_sentiments("https://youtu.be/e-kSGNzu0hM")
    with open("data/iPhone_13_Review_Pros_and_Cons_sentiments.json", "r") as f:
        data = json.load(f)

    positives = []
    negatives = []
    neutrals = []

    for result in data:
        text = result["text"]
        if result["sentiment"] == "POSITIVE":
            positives.append(text)
        elif result["sentiment"] == "NEGATIVE":
            negatives.append(text)
        else:
            neutrals.append(text)


    n_pos = len(positives)
    n_neg = len(negatives)
    n_nut = len(neutrals)

    print("Num positives:", n_pos)
    print("Num negatives:", n_neg)
    print("Num neutrals:", n_nut)

    # ignore neutrals here
    r = n_pos/(n_pos+n_neg)
    print(f"Positive ratio: {r:.3f}")

