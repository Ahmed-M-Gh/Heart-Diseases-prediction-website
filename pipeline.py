import joblib as jb
import numpy as np


class InterFacePipeline:
    def __init__(self):
        
        self.model = jb.load(r'C:\I will prepare my self to destroy the world\Programming\python program\MY Projects\Classification Projects\Heart Diseases\models\LRv1.pkl')
    
    def run(self, input_list):
        input_array = np.asarray(input_list)
        input_array_reshaped = input_array.reshape(1, -1)
        prediction = self.model.predict(input_array_reshaped)
        return prediction