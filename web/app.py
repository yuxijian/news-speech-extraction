#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, make_response
from flask import render_template
from exts import db
from my_config import configs
from models import News
from sqlalchemy import and_, or_, func

app = Flask(__name__)
# app.config.from_object(configs)
app.config['SQLALCHEMY_DATABASE_URI'] = configs.SQLALCHEMY.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = configs.SQLALCHEMY.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news/get', methods=['POST', 'GET'])
def get_news():
    count = db.session.query(func.count(News.id)).scalar()
    totalPages = (count // 10) if (count % 10 == 0) else (count // 10 + 1)

    if request.method == 'POST':
        pageNum = request.form.get("pageNum")
        sql = 'select * from news_chinese order by id limit 1,10;'
        news = db.session.execute(sql)

        return jsonify(list(news))
    else:
        pageNum = request.args.get("pageNum")
        if pageNum is None:
            pageNum = 1
            news = News.query.filter(and_(News.id.__gt__(0), News.id.__lt__(11)))
        else:
            begin = str((int(pageNum) - 1) * 10 + 1)
            sql = 'select * from news_chinese order by id limit ' + begin + ',10;'
            news = db.session.execute(sql)

        newsData = {
            'news': news,
            'totalPages': totalPages,
            'currentPage': pageNum
        }
        return render_template('historynews.html', **newsData)


if __name__ == '__main__':
    app.run()
