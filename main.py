from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def hello_world():
    return f'<h1>Merhaba, websitemize hoşgeldiniz! Alp sayfasına gitmek için <a href="/alp"> buraya </a> tıklayabilirsiniz. Maymun rizz için <a href="/link"> buraya </a></h1>'

@app.route("/alp")
def alp():
    return "<h1> Merhaba benim ismim Alp </h1>"

@app.route("/link")
def rizzlink(): 
    return "<h1> <a> https://www.youtube.com/watch?v=_QMEy8SY2OY </a> </h1>"
    

app.run(debug=True)
