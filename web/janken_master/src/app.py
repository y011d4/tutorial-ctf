import os
import random

from flask import Flask, make_response, redirect, request
import jwt

from secret import FLAG

app = Flask(__name__)
key = os.urandom(32)

DEFAULT_STATE = {"streak": 0}
DEFAULT_STATE_COOKIE = jwt.encode(
    DEFAULT_STATE,
    key=key,
    algorithm="HS256",
)


def judge(player: int, opponent: int):
    if (player + 1) % 3 == opponent:
        return 1  # win
    elif (player - 1) % 3 == opponent:
        return -1  # lose
    else:
        return 0  # draw


def get_streak():
    state = jwt.decode(
        request.cookies.get("state", DEFAULT_STATE_COOKIE),
        key=key,
        algorithms="HS256",
    )
    return state.get("streak", 0)


@app.route("/", methods=["GET"])
def index():
    streak: int
    try:
        streak = get_streak()
    except Exception as e:
        print(e)
        response = make_response("Are you trying to cheat...?", 200)
        response.set_cookie("state", DEFAULT_STATE_COOKIE)
        return response
    message = "You can get a flag if you win 10 times in a row."
    if streak >= 10:
        message = FLAG
    return f"""
    <div>
    Let's Janken!
    {message}<br>
    Current streak: {streak}<br>
    <form method="post" action="/play">
      <input type="radio" id="gu" name="player" value="0" checked><label for="gu">👊</label>
      <input type="radio" id="choki" name="player" value="1"><label for="choki">✌</label>
      <input type="radio" id="pa" name="player" value="2"><label for="pa">✋</label>
      <input type="submit" value="play!">
    </form>
    </div>
    """


@app.route("/play", methods=["POST"])
def play():
    data = request.form
    if "player" not in data:
        return make_response("invalid post", 400)
    streak = get_streak()
    player = int(data["player"])
    opponent = random.randint(0, 2)
    result = judge(player, opponent)
    if result == 1:
        streak += 1
    else:  # draw isn't approved...
        streak = 0
    response = make_response(redirect("/"))
    response.set_cookie(
        "state", jwt.encode({"streak": streak}, key=key, algorithm="HS256")
    )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
