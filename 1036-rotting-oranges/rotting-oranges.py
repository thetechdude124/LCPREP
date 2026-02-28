from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #do one level of bfs for every starting rotten orange position
        #share a visited array state
        #once all have been visited, return the min
        #if we can't visit all of the given oranges return -1

        max_row_idx = len(grid) - 1
        max_col_idx = len(grid[0]) - 1

        visited = set()
        rotten_queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: 
                    rotten_queue.append((i, j))
                    visited.add((i, j))

        def test(curr_row, curr_col, Q, visited):
            if grid[curr_row][curr_col] == 1 and (curr_row, curr_col) not in visited: 
                Q.append((curr_row, curr_col))
                visited.add((curr_row, curr_col))

        #need to store level number (which is the number of minutes)
        #at the beginnig of a level, number of elmenets to process is the number of 
        #elements in the queue
        n_mins = 0
        n_in_level = len(rotten_queue)
        #now, use bfs from all rotten elements and append them to the queue
        while rotten_queue:
            #get rotten cell
            rot_i, rot_j = rotten_queue.popleft()
            n_in_level -= 1

            test_row = [True, True]
            test_col = [True, True]

            if rot_i == 0: test_row[0] = False
            if rot_i == max_row_idx: test_row[1] = False
            if rot_j == 0: test_col[0] = False
            if rot_j == max_col_idx: test_col[1] = False

            if test_row[0]: test(rot_i - 1, rot_j, rotten_queue, visited)
            if test_row[1]: test(rot_i + 1, rot_j, rotten_queue, visited)
            if test_col[0]: test(rot_i, rot_j - 1, rotten_queue, visited)
            if test_col[1]: test(rot_i, rot_j + 1, rotten_queue, visited)

            if n_in_level == 0:
                n_in_level = len(rotten_queue)
                n_mins += 1

        n_mins -= 1 #because when we finish processing the queue we're one larger than needed
            
        #now that all the spreads have been added
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1
        return max(n_mins, 0)
        