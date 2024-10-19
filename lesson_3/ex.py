WINNER_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]]

threat_positions = [[1, 2, 3], [2, 3, 1], [1, 3, 2],
                        [4, 5, 6], [6, 5, 4], [4, 6, 5],
                        [7, 8, 9], [8, 9, 7], [7, 9, 8],
                        [1, 4, 7], [4, 7, 1], [1, 7, 4],
                        [2, 5, 8], [2, 8, 5], [5, 8, 2],
                        [3, 6, 9], [6, 9, 3], [3, 9, 6],
                        [1, 5, 9], [5, 9, 1], [1, 9, 5],
                        [3, 5, 7], [5, 7, 3], [3, 7, 5],]

def test():
    threat_test = [[line[0], line[1], line[2]] 
                   for line in WINNER_LINES]
    threat_test.extend([[line[1], line[2], line[0]] 
                        for line in WINNER_LINES])
    threat_test.extend([[line[0], line[2], line[1]] 
                        for line in WINNER_LINES ])
    print(threat_test == threat_positions)
        
test()