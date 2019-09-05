# live_streaming.py

from flask import url_for,Flask, render_template, Response, stream_with_context,jsonify
import cv2
import face_recog
from dbMgr import *
import time
from datetime import datetime
import socket
from flask_jsglue import JSGlue
import numpy as np
import base64

app = Flask(__name__,static_url_path='/static')
jsglue = JSGlue(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flash')
def video():
    return render_template('index.html')

def gen(fr):
    conn=login_db()
    while True:
        jpg_bytes = fr.get_jpg_bytes(conn)[0]
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')

@app.route('/video_feed')# #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error                                 #뒤에 <int::>적어줘야 파라미터 전달이 된다.
def video_feed():
    
    time.sleep(3)
    print('3초후 시작') 
    return Response(gen(face_recog.FaceRecog()),
            mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/api/info")
def api_info():
    conn = login_db()
    similarity, name, res = select_last(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
@app.route("/api/info2")
def api_info2():
    conn = login_db()
    similarity, name, res = select_last2(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
@app.route("/api/info3")
def api_info3():
    conn = login_db()
    similarity, name, res = select_last3(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
@app.route("/api/info4")
def api_inf4():
    conn = login_db()
    similarity, name, res = select_last4(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
# 여기부터 아래 이미지들
@app.route("/api/info5")
def api_inf5():
    conn = login_db()
    similarity, name, res = select_last(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
@app.route("/api/info6")
def api_inf6():
    conn = login_db()
    similarity, name, res = select_last2(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
@app.route("/api/info7")
def api_inf7():
    conn = login_db()
    similarity, name, res = select_last3(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
@app.route("/api/info8")
def api_inf8():
    conn = login_db()
    similarity, name, res = select_last4(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
@app.route("/api/info9")
def api_inf9():
    conn = login_db()
    similarity, name, res = select_last5(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
@app.route("/api/info10")
def api_inf10():
    conn = login_db()
    similarity, name, res = select_last6(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
@app.route("/api/info11")
def api_inf11():
    conn = login_db()
    similarity, name, res = select_last7(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)
@app.route("/api/info12")
def api_inf12():
    conn = login_db()
    similarity, name, res = select_last8(conn)
    encoded_image = base64.b64encode(res)
    info = {
       "image" : "%s"%encoded_image,
       "description" : "%s"%name,
       "description2" : "%s"%similarity,
    }
    return jsonify(info)



@app.route('/tmp')
def tmp():
    lst = [];
    name = [];
    similarity = [];
    conn = login_db()
    for i in range(2,100):
        lst.append( "<img src=\"http://%s:5000/get_img/%s\" width='200' height='200'>"%(socket.gethostbyname(socket.getfqdn()),i))
        name.append(select_img(conn,i)[1])
        similarity.append(select_img(conn,i)[2])
    print(name)
    print(similarity)
    return render_template('webView5.html',item=lst, item2=name, item3=similarity)

@app.route('/modal')
def modal():
    return render_template('modal.html')

@app.route('/Ronaldo')
def Ronaldo():
    return render_template('Ronaldo.html')
@app.route('/messy')
def messy():
    return render_template('messy.html')    



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

