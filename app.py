import queue
import sounddevice as sd
import voice as voice
import vosk
import json
import words

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


q = queue.Queue()
model = vosk.Model('model_small')
device = sd.default.device = 0, 4
samplerate = int(sd.query_devices(device[0], 'input', )['default_samplerate'])


# 48000
def callback(indata, frames, time, status):
    q.put(bytes(indata))


def recognize(data, vectorizers, clf):
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return
    data.replase(list(trg)[0], '')
    text_vector = vectorizers.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    func_name = answer.split()[0]
    voice.speaker(answer.replace(func_name, ''))
    exec(func_name + '()')


def main():
    vectorized = CountVectorizer
    vectorss = (words.data_set.keys())
    vectors = vectorss.fit_transform(list())
    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values))
    del words.data_set
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device,
                           dtype="int16", channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
            recognize(data, vectorized, clf)
            if __name__ == '__main__':
                main()
