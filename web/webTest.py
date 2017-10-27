# -*- coding: utf-8 -*-
import web
from web.contrib.template import render_jinja

urls=(
    '/(.*)','Index'
)

render = render_jinja('templates/')

class Index:
    def GET(self,name):
        i = web.input(name=None)
        print name+'*'
        return  render.test(i.name)

app = web.application(urls,globals())

if __name__ == '__main__':
    app.run()
