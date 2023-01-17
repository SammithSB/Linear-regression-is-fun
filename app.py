import flask
from flask import Flask, render_template, request, redirect, json
import numpy as np


app = Flask(__name__)


def est_coeff(x, y):
    # number of observations
    n = np.size(x)
    # mean of x and y
    mx = np.mean(x)
    my = np.mean(y)
    # calculating deviaition
    xy = np.sum(y*x)-n*mx*my
    xx = np.sum(x*x)-n*mx*mx
    # coefficients
    b1 = (xy)/(xx)
    b0 = my-b1*mx
    return (b1, b0, xy, xx)


def list_input(new_input):
    new_input = new_input.split(',')
    new = []
    for i in new_input:
        new.append(float(i))
    new = np.array(new)
    return new


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/calc', methods=['GET', 'POST'])
def result():
    xval = request.form['x_values']
    yval = request.form['y_values']
    try:
        xval1 = list_input(xval)
        yval1 = list_input(yval)
        data = est_coeff(xval1, yval1)
        coef = []
        for i in data:
            coef.append(float(i))
        xv = np.ndarray.tolist(xval1)
        yv = np.ndarray.tolist(yval1)
        return render_template('result.html', new=coef, x=xv, y=yv)
    except:
        return render_template('error.html', xvalue=xval, yvalue=yval)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
