# coding: utf-8

from flask import Flask, render_template, request, flash, redirect
import logging
from leancloud import Query
import random

from models import ZhuangBiRecord
import wechat_run

app = Flask(__name__)
app.secret_key = 'werun'


logging.basicConfig(level=logging.INFO)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        ldl_id = data.get('ldl_id')
        steps = data.get('steps')
        if not wechat_run.isnum(steps):
            flash(u'要修改的步数不正确~')
            return redirect('/')
        steps = int(steps)
        status_code, content = wechat_run.main(steps, ldl_id)
        if status_code == 200:
            record = ZhuangBiRecord()
            record.set('ldl_id', ldl_id)
            record.set('steps', steps)
            record.save()
            flash(u'修改成功~完成装逼!')
            return redirect('/')
        else:
            flash(u'修改失败~')
            return redirect('/')
    count = Query(ZhuangBiRecord).count()
    return render_template('index.html', count=count)


@app.route('/help')
def help():
    return render_template('help.html')
