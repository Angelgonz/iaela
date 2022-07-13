from importlib.resources import path
from flask import Flask,jsonify,render_template
from numpy import size
from requests import get
import matplotlib.pyplot as plt
import os,shutil
import cv2

app = Flask(__name__)

@app.route('/recibir')
def maquetando():
    recibir=get("https://aples.herokuapp.com/mail").json()

    print(recibir["Prediccion"])
    
    #return jsonify(recibir)
    fig, ax = plt.subplots()
    la='num. Spam','num. Ham'
    ax.pie([recibir["spam"],recibir["ham"]],labels=la)
    #plt.show()
    os.remove("static/img/graficar.png")
    spath="static/img/"
    plt.savefig(os.path.join(spath,"graficar.png"))
    
    return render_template("mostrar.html",recibir=recibir)
if __name__=="__main__":
    app.run(debug=True,port=3000)