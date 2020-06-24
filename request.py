# -*- coding: utf-8 -*-
 
import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={['Pregnancies':1, 'Glucose':148, 'BloodPressure':72, 'SkinThickness':31 ,	'Insulin': 88,	'BMI':25.6 ,	'DiabetesPedigreeFunction':1.567 ,	'Age':60]})

print(r.json())