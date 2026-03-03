import numpy as np
from collections import Counter
# https://www.emergentmind.com/topics/gaussian-based-knn-resampling-gkr

class Gaussian:
    def __init__(self, weight = 1.0):
        self.weight = weight
        self.x_training_set = None
        self.y_training_set = None
        
    def fit(self, x_train, y_train):
        self.x_training_set = np.array(x_train)
        self.y_training_set = np.array(y_train)

    def get_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2)) 

    def gaussian_weight(self, dist):
        return np.exp(-(dist ** 2)/ (2 * self.weight ** 2))
    
    def gaussian_decide_label(self, k_nearest_labels):
        weighted_count = {}
        
        for dist, i in k_nearest_labels:
            label = self.y_training_set[i]
            weight = self.gaussian_weight(dist)
            
            if label not in weighted_count:
                weighted_count[label] = 0
            
            weighted_count[label] += weight

        max_num = 0
        max_label = ""
        for label, num in weighted_count.items():
            if num > max_num:
                max_num = num
                max_label = label
        
        return max_label
    
    def test (self, test_set):
        test_set = np.array(test_set) 
        return [self.predict(test) for test in test_set]

    def predict (self, input):
        dist_labels = []
        for x_train in self.x_training_set:
            dist_labels.append((self.get_distance(input, x_train), i))

        return self.gaussian_decide_label(dist_labels)
    
    # def metrics (self, y_correct, y_predicted):
    # TODO: write after knowing the data more!!!
    #     for i in range(len(y_correct)):
    #         y_c = y_correct[i]
    #         y_p = y_predicted[i]

    #         if y_c == y_p:
    #             true_pos += 1
    #         elif y_c == 
