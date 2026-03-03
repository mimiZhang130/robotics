import numpy as np
import heapq
from collections import Counter

neighbors = 5

class KNN:
    def __init__(self, k=neighbors, weight = 1.0):
        self.k = k
        self.weight = weight
        self.x_training_set = None
        self.y_training_set = None
    
    def fit(self, x_train, y_train):
        self.x_training_set = np.array(x_train)
        self.y_training_set = np.array(y_train)

    def get_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2)) 

    def knn_decide_label(self, k_nearest_labels):
        num_labels = Counter(k_nearest_labels)
        max_num = 0
        max_label = ""
        for label, num in num_labels.items():
            if num > max_num:
                max_num = num
                max_label = label
        
        return max_label
    
    def test (self, test_set):
        test_set = np.array(test_set) 
        return [self.predict(test) for test in test_set]

    def predict (self, input):
        distances = []
        for x_train in self.x_training_set:
            distances.append(self.get_distance(input, x_train))
        
        k_nearest_neighbors = []

        for i, dist in enumerate(distances):
            heapq.heappush(k_nearest_neighbors, (-dist, i))
            
            if len(k_nearest_neighbors) > self.k:
                heapq.heappop(k_nearest_neighbors)
        
        k_nearest_labels = [self.y_training_set[i] for (-dist, i) in k_nearest_neighbors]
        
        return self.knn_decide_label(k_nearest_labels)
    
