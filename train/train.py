import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib as jb

print('[Loading Data]start loading data...')
data = pd.read_csv(r'C:\I will prepare my self to destroy the world\Programming\python program\MY Projects\Classification Projects\Heart Diseases\train\heart_disease_data.csv')
print('[Loading Data] data loaded successfully')

print('[Splitting Data]start splitting data...')
X = data.drop('target', axis=1)
Y = data['target']
print('[Splitting Data]splitting data completed successfully')

print('[Training]start model training...')
model = LogisticRegression(max_iter=10000)
model.fit(X, Y)
print('[Training]model training completed successfully!')


print('[Saving]start saving model...')
jb.dump(model, r'C:\I will prepare my self to destroy the world\Programming\python program\MY Projects\Classification Projects\Heart Diseases\models\LRv1.pkl')