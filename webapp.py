from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("keypress_v2.html")

@app.route("/bigrams", methods=["POST"])
def show_bigrams():
    freq = request.form.get("freq")
    count = request.form.get("count")
    strokes = request.form.get("stroke")
    timestamps = model.get_timestamps(strokes)
    bigrams = model.find_bigrams(timestamps)
    return render_template("bigrams.html", freq=freq, count=count, strokes=strokes, 
                            timestamps=timestamps, bigrams=bigrams)


if __name__ == "__main__":
    app.run(debug=True)