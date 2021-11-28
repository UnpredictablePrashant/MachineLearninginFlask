from flask import Flask, request
from flask.templating import render_template
from model import summariser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=["POST"])
def summary():
    if request.method == "POST":
        data = request.form.to_dict()
        text = data['review_text']
        finalResult = summariser(text)
        #finalResult = finalResult.append()
    return render_template("results.html", summary = finalResult)
if __name__ == "__main__":
    app.run(debug=True, port=8000)