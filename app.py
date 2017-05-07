from flask import Flask
from flask import render_template, redirect, url_for

app=Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html')


@app.route('/save', methods=['POST'])
def save():
	return "saved!"

app.run(debug=True)