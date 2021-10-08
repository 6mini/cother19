from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("data/pkl/lgb.pkl", "rb"))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
    
        return render_template('index.html')

    if request.method == 'POST':

        data1 = float(request.form['avgRhm'])
        data2 = float(request.form['ddMes'])
        data3 = float(request.form['sumSsHr'])
        data4 = float(request.form['avgPs'])
        data5 = float(request.form['avgTca'])
        data6 = float(request.form['avgTd'])
        data7 = float(request.form['minTa'])
        data8 = float(request.form['maxTa'])
        data9 = float(request.form['avgWs'])
        data10 = float(request.form['sumRn'])
        data11 = float(request.form['avgTa'])

        arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]])
        pred = model.predict(arr)
        pred = round(pred[0])


        return render_template("index.html", pred=pred)


if __name__ == "__main__":
    app.run(debug=True)
