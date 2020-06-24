import numpy as np
from flask import Flask,render_template,request,jsonify
from sklearn.externals import joblib
import pickle
import json
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize

 



 
 
app =Flask(__name__)
model=pickle.load(open('modelrandomforest.pkl','rb'))
#model,means, stds=joblib.load('diabeteseModel.pkl')
@app.route('/')
def  page():
 return render_template('secondpage.html')

   
@app.route('/predict', methods=['POST'])  
def predict():
   # For rendering results on HTML GUI
     formvalues = request.form
     path1 = "/json/"
     with open(os.path.join(os.getcwd()+"/"+path1,'file.json'), 'w') as f:
        json.dump(formvalues, f)
     with open(os.path.join(os.getcwd()+"/"+path1,'file.json'), 'r') as f:
        values = json.load(f)
        df = pd.DataFrame(json_normalize(values))
         
        model_path=os.getcwd()+"/modelrandomforest.pkl"
        model =joblib.load(model_path) 
        ##means = np.mean(df )
       ## stds = np.std(df )
        ##df = (df - means)/stds
        result = model.predict(df)
        a=np.array(1)
        #b=a.astype('int')
        if result.astype('int')==a.astype('int'):##comparing with 1
          msg="Success"
        else:
          msg = "Unsuccess"
        #positive_percent= model.predict_proba(df)[0df][1]*100
        #return render_template("secondpage.html",msg=msg,prob=positive_percent,**request.args)
        return render_template("secondpage.html",msg=msg)


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

 

if __name__ == "__main__":
    app.run(debug=True)
  
 