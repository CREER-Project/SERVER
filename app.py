# 2022 / 11 / 6 writing sourceCode.
# copyright (c) 2022 @gamma410 All rights reserved.
# CRÉER Live Streaming Platform.
# This sourceCode is CRÉER's serverSystem.

from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from json_serializable import JSONSerializable # SpecialThanks...!


# Random String
import random, string
def randomString(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

# Date Get
import datetime
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)


app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)

JSONSerializable(app) # SpecialThanks...!

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///postData.db'
app.config['SCRET_KEY'] = '5730292743938474948439320285857603'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    videoDetail = db.Column(db.Text, nullable=False)
    videoTitleHex = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer) # 1 = OPEN / 2 = CLOSE


@app.route('/')
def index():
    lives = Post.query.filter_by(status=1).order_by(Post.id.asc()).all()

    return jsonify(lives)


@app.route('/lives/<int:id>')
def lives(id):
    lives = Post.query.filter_by(id=id).order_by(Post.id.asc()).all()

    return jsonify(lives)

@app.route('/post', methods=['GET','POST'])
def post():
    if request.method == "POST":
        userName = request.args['userName']
        title = request.args['title']
        videoDetail = request.args['videoDetail']
        videoHex1 = randomString(10)
        videoHex2 = now.strftime('%Y%m%d%H%M%S')
        videoTitleHex = videoHex1 + "-" + videoHex2
        status = 1

        createPost = Post (
            userName = userName,
            title = title, 
            videoDetail = videoDetail,
            videoTitleHex = videoTitleHex,
            status = status
        )

        db.session.add(createPost)
        db.session.commit()

        return "POST"

    else:
        return ""

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    liveId = request.args['id']

    removePost = Post.query.get(liveId)

    db.session.delete(removePost)
    db.session.commit()

    return redirect('')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)