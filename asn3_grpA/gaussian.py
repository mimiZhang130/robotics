import math
from collections import Counter
# https://www.emergentmind.com/topics/gaussian-based-knn-resampling-gkr
from data import create_data, maze_x_data, maze_y_data, out_maze_x_data, out_maze_y_data, split_data, test_data

class Gaussian:
    def __init__(self, weight = 1.0):
        self.weight = weight
        self.x_training_set = None
        self.y_training_set = None
        
    def fit(self, x_train, y_train):
        self.x_training_set = x_train
        self.y_training_set = y_train

    def get_distance(self, x1, x2):
        res = (x1 - x2) ** 2
        return math.sqrt(res)

    def gaussian_weight(self, dist):
        return math.exp(-(dist ** 2)/ (2 * self.weight ** 2))
    
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
    
    def predict (self, input):
        dist_labels = []
        for i, x_train in enumerate(self.x_training_set):
            dist_labels.append((self.get_distance(input, x_train[0]), i))

        return self.gaussian_decide_label(dist_labels)

weight = .4

def run_gaussian_maze(weight = weight):
    gaussian = Gaussian(weight) 

    gaussian.fit(maze_x_data, maze_y_data) 

    return gaussian

def run_gaussian_out_maze(weight = weight):
    gaussian = Gaussian(weight) 
    
    gaussian.fit(out_maze_x_data, out_maze_y_data) 

    return gaussian

def run_gaussian_combo(maze, out_maze, out_maze_2, weight = weight):
    gaussian = Gaussian(weight) 
    
    x_data, y_data = create_data(maze, out_maze, out_maze_2)

    gaussian.fit(x_data, y_data) 

    return gaussian

def tune_sigma():
    # perform cross validation
    weights = [0, 0.2, 0.4, 0.6, 0.8, 1]
    best_weight = None
    best_avg_err = 100 # too high of an error for anything to reach so it's safe
    for w in weights:
        gaussian = Gaussian(.4)
        x_train, y_train, x_test, y_test = split_data(x_data, y_data)
        # x_train, y_train, x_test, y_test = split_data(maze_x_data, maze_y_data)
        gaussian.fit(x_train, y_train)
        [accuracy, avg_error] = test_data(x_test, y_test, gaussian)
        if avg_error < best_avg_err:
            best_weight = weight
    
    print(best_weight)

if __name__ == '__main__':
    # tune_sigma()
    model = run_gaussian_out_maze()
    print(model.predict(10.2))