from json import JSONDecodeError

from flask import Flask, jsonify, render_template
from file_helper import load_json

app = Flask(__name__)


@app.route("/")
def index():
    file_path = "blog_posts.json"
    try:
        blog_posts = load_json(file_path)
    except (FileNotFoundError, PermissionError, JSONDecodeError, Exception) as error:
        app.logger.exception(f"Error occured: {error}")
        return ("Internal Server Error", 500)
    else:
        return render_template("index.html", posts=blog_posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
