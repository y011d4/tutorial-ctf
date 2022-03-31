from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return """
    <div>
    This is a web app that enables to render your note from a simple query!
    <a href="/render?title=Example&content=NOTE: My secret file is at /app/flag.txt :)">Example</a>
    </div>
    <div>
    You can also use this as a simple calculator using power of Jinja2.
    <a href="/render?title=Example&content=1337 * 1337 = {{1337 * 1337}}">Example</a>
    </div>
    """


@app.route("/render", methods=["GET"])
def render():
    title = request.args.get("title", "Example Note")
    content = request.args.get("content", "lorem ipsum")
    return render_template_string(f"<h1>{title}</h1><p>{content}</p>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
