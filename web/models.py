#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Models for user, blog, comment.
"""

__author__ = 'yxj'

from exts import db


class News(db.Model):
    __tablename__ = 'news_chinese'  # 表名设置为user
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(32), nullable=True)
    source = db.Column(db.String(32), nullable=True)
    content = db.Column(db.String(1000), nullable=True)
    feature = db.Column(db.String(256), nullable=True)
    title = db.Column(db.String(32), nullable=True)
    url = db.Column(db.String(32), nullable=True)
