# -*- coding: utf-8 -*-

import os

import leancloud
from wsgiref import simple_server


APP_ID = 'p5wg1h2JLLqAM4KYBsC1LYht-gzGzoHsz'
MASTER_KEY = 'tThlPa3ROnEiYmbiiD8lSlTY'
PORT = 3000


leancloud.init(APP_ID, master_key=MASTER_KEY)
from app import app
from cloud import engine
application = engine


if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    app.debug = True
    server = simple_server.make_server('localhost', PORT, application)
    server.serve_forever()
