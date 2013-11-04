class Keypress(object):
    def __init__(self, key, timestamp):
        self.key = key
        self.timestamp = timestamp
        self.difference = 0
        self.bigram = []


def get_timestamps(strokes):
    timestamps = []
    strokes = str(strokes).strip()
    strokes = strokes[1:-2]
    keystrokes = strokes.split("|")
    for stroke in keystrokes:
        stamp = stroke.split()
        press = Keypress(int(stamp[0]), int(stamp[1]))
        timestamps.append(press)
    for i in range(len(timestamps)):
        if i == 0:
            timestamps[i].difference = 0
        else:
            previous = timestamps[i-1]
            current = timestamps[i]
            current.difference = abs(previous.timestamp - current.timestamp)
    return timestamps

def find_bigrams(timestamps):
    bigrams = []
    for i in range(len(timestamps)):
        if i < (len(timestamps) - 1):
            bigrams.append((timestamps[i].key, timestamps[i+1].key))
    return bigrams