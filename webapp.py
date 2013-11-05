from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("keypress_v3.html")

@app.route("/bigrams", methods=["POST"])
def show_bigrams():
    text = request.form.get("text")
    raw_text = request.form.get("rawtext")
    strokes = request.form.get("stroke")
    timestamps = model.get_timestamps(strokes)
    bigrams = model.find_bigrams(timestamps)
    return render_template("bigrams.html", strokes=strokes, 
                            timestamps=timestamps, bigrams=bigrams, text=text, raw_text=raw_text)


if __name__ == "__main__":
    app.run(debug=True)