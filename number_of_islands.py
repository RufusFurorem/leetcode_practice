def numIslands(grid) -> int:
    visited_vertices = {}
    bfs_queue = []
    num_island = 0
    if not grid:
        return 0
    num_rows = len(grid) - 1
    num_cols = len(grid[0]) - 1

    for i in range(len(grid)):
        for k in range(len(grid[0])):

            if grid[i][k] == '1':
                bfs_queue.append((i, k))
                visited_vertices[(i, k)] = True
                grid[i][k] = '0'

                while bfs_queue:

                    curr_vertex = bfs_queue.pop(0)
                    search_above = grid[max(0,(curr_vertex[0] - 1))][curr_vertex[1]]
                    search_above_tuple  = (max(0,(curr_vertex[0] - 1)), curr_vertex[1])

                    search_below = grid[min(num_rows, (curr_vertex[0] + 1))][curr_vertex[1]]
                    search_below_tuple = (min(num_rows, (curr_vertex[0] + 1)), curr_vertex[1])

                    search_left  = grid[curr_vertex[0]][max(0,(curr_vertex[1] - 1))]
                    search_left_tuple = (curr_vertex[0], max(0,(curr_vertex[1] - 1)))

                    search_right = grid[curr_vertex[0]][min(num_cols,(curr_vertex[1] + 1))]
                    search_right_tuple = (curr_vertex[0], min(num_cols,(curr_vertex[1] + 1)))

                    if search_above == '1' and search_above_tuple not in visited_vertices:
                        bfs_queue.append(search_above_tuple)
                        visited_vertices[search_above_tuple] = True
                        grid[search_above_tuple[0]][search_above_tuple[1]] = '0'

                    if search_below == '1' and search_below_tuple not in visited_vertices:
                        bfs_queue.append(((curr_vertex[0] + 1), curr_vertex[1]))
                        visited_vertices[((curr_vertex[0] + 1), curr_vertex[1])] = True
                        grid[search_below_tuple[0]][search_below_tuple[1]] = '0'

                    if search_left == '1' and search_left_tuple not in visited_vertices:
                        bfs_queue.append((curr_vertex[0], (curr_vertex[1] - 1)))
                        visited_vertices[(curr_vertex[0], (curr_vertex[1] - 1))] = True
                        grid[search_left_tuple[0]][search_left_tuple[1]] = '0'

                    if search_right == '1' and search_right_tuple not in visited_vertices:
                        bfs_queue.append((curr_vertex[0], (curr_vertex[1] + 1)))
                        visited_vertices[(curr_vertex[0], (curr_vertex[1] + 1))] = True
                        grid[search_right_tuple[0]][search_right_tuple[1]] = '0'

                num_island += 1

    return num_island


if __name__ == "__main__":
    
    island_map = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    ret_val = numIslands(island_map)
    print(ret_val)
