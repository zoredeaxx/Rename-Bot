from flask import Flask
from threading import Thread
import datetime


app = Flask('')


@app.route('/')

def home():

    content = "<p>" + "Online @ " + str(datetime.datetime.now()) + "</p>"
    return content
    #return f"<h1>😎I'm Awake Already!🔥</h1>"

def run():

  app.run(host='0.0.0.0',port=8080)



def keep_alive():  

    t = Thread(target=run)

    t.start()

keep_alive()
