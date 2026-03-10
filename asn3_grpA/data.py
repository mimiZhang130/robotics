import random # https://www.w3schools.com/python/ref_random_shuffle.asp

maze_x_data = [
            [11.14016667],
            [10.99433333],
            [11.03566667],
            [10.88016667],
            [10.9385],
            [10.785],
            [10.61866667],
            [10.149],
            [10.0604],
            [9.895],
            [9.7986],
            [9.6944],
            [9.476],
            [9.052],
            [8.8474],
            [10.7082],
            [10.9114],
            [10.9995],
            [9.673],
            [9.852333333],
            [9.862666667],
            [9.9294],
            [9.938],
            [9.9552],
            [10.198],
            [10.20133333],
            [10.27366667],
            [10.28866667],
            [10.4822],
            [10.4892],
            [10.63733333],
            [10.643],
            [10.729],
            [10.8682]
            ]

maze_y_data =   [
            (-8, -8),
            (-9, -9),
            (-9, -8),
            (-9, -10),
            (-8, -8),
            (-8, -8),
            (-9, -10),
            (-4, -4),
            (-3, -3),
            (-3, -3),
            (-3, -3),
            (-2, -2),
            (-2, -3),
            (-5, -5),
            (-3, -2),
            (-7, -8),
            (-7, -8),
            (-8, -8),
            (-2, -2),
            (-1, -1),
            (0, 0),
            (-1, 0),
            (-2, -2),
            (-2, -2),
            (-5, -5),
            (-5, -5),
            (-4, -5),
            (-5, -5),
            (-7, -7),
            (-7, -7),
            (-9, -9),
            (-8, -8),
            (-9, -8),
            (-9, -9)
            ]

out_maze_x_data = [
                    [11.32183333],
                    [11.31466667],
                    [8.44],
                    [8.690666667],
                    [8.896],
                    [9.262333333],
                    [9.571],
                    [9.728],
                    [9.730666667],
                    [10.07733333],
                    [10.0918],
                    [10.1054],
                    [10.209],
                    [10.2688],
                    [10.4414],
                    [10.5062]
                   ]

out_maze_y_data = [(-4, -4),
                   (-5, -5),
                   (-6, -6),
                   (-8, -9),
                   (-9, -8),
                   (-7, -7),
                   (-5, -5),
                   (-4, -4),
                   (-4, -4),
                   (-1,	-1),
                   (1, 1),
                   (0, 0),
                   (2, 1),
                   (1, 2),
                   (-2, -1),
                   (-3, -3)
                   ]

out_maze_2_x_data = [
        [10.6794],
        [10.5282],
        [10.5108],
        [11.045],
        [11.557],
        [11.30566667],
        [11.10333333],
        [10.95916667],
        [10.9765],
        [10.87033333],
        [10.92525],
        [10.71975],
        [10.73875],
        [10.71633333],
        [10.482],
        [10.2785],
        [10.23366667],
        [10.2515],
        [10.01933333]
]

out_maze_2_y_data = [
    (-4, -3),
    (-4, -4),
    (-4, -4),
    (-5, -5),
    (0,	0),
    (-5, -4),
    (-6, -6),
    (-7, -7),
    (-8, -7),
    (-7, -8),
    (-7, -7),
    (-8, -8),
    (-8, -8),
    (-7, -7),
    (-7, -7),
    (-9, -9),
    (-10, -10),
    (-10, -10),
    (-10, -11)
]

def create_data(maze, out_maze, out_maze_2):
    x_data = []
    y_data = []
    if maze:
        for i in maze_x_data:
            x_data.append(i)
        for i in maze_y_data:
            y_data.append(i)
    if out_maze:
        for i in out_maze_x_data:
            x_data.append(i)
        for i in out_maze_y_data:
            y_data.append(i)
    if out_maze_2:
        for i in out_maze_2_x_data:
            x_data.append(i)
        for i in out_maze_2_y_data:
            y_data.append(i)
    return (x_data, y_data)

def split_data (x, y, test_split = .2):
        data = list(zip(x, y)) # keep data together
        random.shuffle(data) # shuffle the data

        split = int(len(data) * (1 - test_split)) # find where data should be split 
        train_data = data[:split]
        test_data = data[split:]

        # make train sets
        x_train = [d[0] for d in train_data]
        y_train = [d[1] for d in train_data]

        # make test sets
        x_test = [d[0] for d in test_data]
        y_test = [d[1] for d in test_data]
        
        # return all sets
        return x_train, y_train, x_test, y_test

def test_data (x_test, y_test, model):
    correct = 0
    tot_err = 0
    for test_input, actual_label in zip(x_test, y_test):
        pred = model.predict(test_input[0])
        print(f"pred: {pred}, actual: {actual_label}")
        if pred == actual_label:
            correct += 1
        hip4_err = abs(pred[0] - actual_label[0])
        hip6_err = abs(pred[1] - actual_label[1])

        tot_err += (hip4_err + hip6_err) 
    
    accuracy = correct / len(x_test)
    avg_err = tot_err / (len(x_test) * 2)
    print(f"accuracy: {accuracy}")
    print(f"avg_err: {avg_err}")
    return [accuracy, avg_err]