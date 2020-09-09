from flask import Flask, render_template, redirect, flash, request, url_for
from forms import NameForm
import json, random, re
import os
import socket

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

compliment_dict = {}
with open('app/dict.txt', 'r') as file:
    compliment_dict = json.loads(file.read())

@app.route('/', methods=['GET', 'POST'])
def get_name():
    form = NameForm(request.form)
    if form.validate_on_submit(): 
        name = form.name.data
        return redirect(url_for('.get_compliment', name=name))
    return render_template('name.html', form=form)


@app.route('/compliment', methods=['GET', 'POST'])
def get_compliment():
    name = request.args['name'].upper()
    name_dict = []
    for n in name:
        compliment = random.choice(compliment_dict[n]).upper()
        pair = [n, compliment]
        name_dict.append(pair)
    return render_template('compliment.html', name=name_dict)

if __name__ == "__main__":
    app.run(host="0.0.0.0")