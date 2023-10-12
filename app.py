from flask import Flask,redirect,url_for,render_template,request, jsonify
import os
from os.path import join, dirname
from dotenv import load_dotenv

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run('0.0.0.0', 5000,debug=True)