import Astar
import AOstar
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--algorithm', default='Astar', type=str)
    opt = parser.parse_args()
    assert opt.algorithm in ['Astar', 'AOstar']

    if opt.algorithm == 'Astar':
        # 0：屏障 1：可走 2：起点 3：终点 4：已访问点 5：访问边界
        while 1:
            game_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                        [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
                        [0, 2, 1, 0, 1, 1, 1, 0, 1, 3, 1, 1, 0],
                        [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            Astar.draw_map(game_map)
            Astar.Astar(game_map, (3, 1), (3, 9))
    else:
        while 1:
            nodes_tree = {}
            nodes_tree[0] = [[1], [4, 5]]
            nodes_tree[1] = [[2], [3]]
            nodes_tree[2] = [[3], [2, 5]]
            nodes_tree[3] = [[5, 6]]
            nodes_tree[4] = [[5], [8]]
            nodes_tree[5] = [[6], [7, 8]]
            nodes_tree[6] = [[7, 8]]
            nodes_tree[7] = [[7]]
            nodes_tree[8] = [[8]]
            h_val = [3, 2, 4, 4, 1, 1, 2, 0, 0]
            AOstar.AOstar(nodes_tree, h_val)
