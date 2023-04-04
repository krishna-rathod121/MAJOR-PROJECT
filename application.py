from flask import Flask, render_template, request
import pickle
import numpy as np


app=Flask(__name__)


model = pickle.load(open("LinearRegressionModell.pkl", 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predicts',methods=['post'])
def predicts():
    ball_size= int(request.form.get('ball_size'))
    ball_load=int(request.form.get('ball_load'))
    charge_ratio=float(request.form.get('ball_charge'))
    grinding_time=int(request.form.get('ball_time'))
    

    predictions = model.predict(np.array([[ball_size, ball_load, charge_ratio, grinding_time]]))
    
    return str(predictions)
    



if __name__=="__main__":
    app.run(debug=True)