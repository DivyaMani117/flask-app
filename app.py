#!python3

from flask import Flask

app = Flask(_name_)
@app.route('/')
def welcome():
    return 'This is my first Flask! Yay!'
    
app.run()