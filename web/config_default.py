#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Default configurations.
"""

__author__ = 'yxj'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'ai_study'
    },
    'session': {
        'secret': 'ai_commando'
    },
    'SQLALCHEMY': {
        'SQLALCHEMY_DATABASE_URI':
            'mysql://root:AI@2019@ai@rm-8vbwj6507z6465505ro.mysql.zhangbei.rds.aliyuncs.com/stu_db',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }

}
