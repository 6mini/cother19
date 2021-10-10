import pickle
import numpy as np
 
model = pickle.load(open("lgb.pkl", "rb"))

arr = np.array([[57.3,0.0,10.5,1018.2,2.3,4.8,8.5,18.4,2.5,0.0,13.3]])
pred = model.predict(arr)
print(pred)