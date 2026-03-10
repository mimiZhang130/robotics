import math
import heapq
from collections import Counter
from data import x_data, y_data, maze_x_data, maze_y_data, out_maze_x_data, out_maze_y_data, split_data, test_data

neighbors = 5

class KNN:
    def __init__(self, k=neighbors,):
        self.k = k
        self.x_training_set = None
        self.y_training_set = None
    
    def fit(self, x_train, y_train):
        self.x_training_set = x_train
        self.y_training_set = y_train

    def get_distance(self, x1, x2):
        res = (x1 - x2) ** 2
        return math.sqrt(res)

    def knn_decide_split_label(self, k_nearest_labels):
        num_labels = Counter(k_nearest_labels)
        max_num = 0
        max_label = ""
        for label, num in num_labels.items():
            if num > max_num:
                max_num = num
                max_label = label
        return max_label

    def predict (self, input):
        distances = []
        for x_val in self.x_training_set:
            distances.append(self.get_distance(input, x_val[0]))
        
        k_nearest_neighbors = []

        for i, dist in enumerate(distances):
            neg_dst = -1 * dist
            heapq.heappush(k_nearest_neighbors, (neg_dst, i))
            
            if len(k_nearest_neighbors) > self.k:
                heapq.heappop(k_nearest_neighbors)
        
        k_nearest_hip4_labels = [self.y_training_set[i][0] for (neg_dst, i) in k_nearest_neighbors]
        k_nearest_hip6_labels = [self.y_training_set[i][1] for (neg_dst, i) in k_nearest_neighbors]
        hip4 = self.knn_decide_split_label(k_nearest_hip4_labels)
        hip6 = self.knn_decide_split_label(k_nearest_hip6_labels)

        return (hip4, hip6)

def run_knn_maze(neighbors=neighbors):
    knn = KNN(neighbors) 

    knn.fit(maze_x_data, maze_y_data) 

    return knn

def run_knn_out_maze(neighbors=neighbors):
    knn = KNN(neighbors) 
    
    knn.fit(out_maze_x_data, out_maze_y_data) 

    return knn

def run_knn_all(neighbors=neighbors):
    knn = KNN(neighbors) 
    
    knn.fit(x_data, y_data) 

    return knn

if __name__ == '__main__':

    knn = KNN(neighbors)
    x_train, y_train, x_test, y_test = split_data(x_data, y_data)
    # x_train, y_train, x_test, y_test = split_data(maze_x_data, maze_y_data)

    knn.fit(x_train, y_train)

    test_data(x_test, y_test, knn)
    
    



