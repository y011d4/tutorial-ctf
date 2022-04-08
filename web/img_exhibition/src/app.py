import os

from flask import Flask, make_response, request

from crawler import crawl
from utils import make_exhibition_page

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return """
    <div>
    <form method="get" action="/preview">
      <div>
        <label for="url">URL: </label><input type="text" id="url" name="url" value="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png">
        <label for="title">title: </label><input type="text" id="title" name="title" value="Google">
      </div>
      <div>
        <button type="submit" formaction="/preview" formmethod="get">preview</button>
        <button type="submit" formaction="/report" formmethod="post">report</button>
      </div>
    </form>
    </div>
    """


@app.route("/preview", methods=["GET"])
def preview():
    args = request.args
    if "url" not in args or "title" not in args:
        return make_response("Please specify url and title!", 400)
    url = args["url"]
    title = args["title"]
    return make_exhibition_page(url, title)


@app.route("/report", methods=["POST"])
def report():
    data = request.form
    if "url" not in data or "title" not in data:
        return make_response("Please specify url and title!", 400)
    url = data["url"]
    title = data["title"]
    crawl(url, title)  # admin will see /preview?url={url}&title={title}
    return make_response("Done!", 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
