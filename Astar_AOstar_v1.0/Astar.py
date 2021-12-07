import heapq
import os
import time


class PriorityQueue:
    def __init__(self):
        self.priorityqueue = []
        self.index = 0

    def add(self, item, priority):
        heapq.heappush(self.priorityqueue, (-priority, self.index, item))
        self.index += 1
        return

    def pop(self):
        return heapq.heappop(self.priorityqueue)[-1]


def draw_map(game_map):
    os.system('cls')

    for i in range(len(game_map)):
        for j in range(len(game_map[0])):
            if game_map[i][j] == 0:
                print("\033[0;31;40;1m■ \033[0m", end='')
            elif game_map[i][j] == 1:
                print("\033[0;37;40;1m□ \033[0m", end='')
            elif game_map[i][j] == 2:
                print("\033[0;33;40;1m■ \033[0m", end='')
            elif game_map[i][j] == 3:
                print("\033[0;35;40;1m■ \033[0m", end='')
            elif game_map[i][j] == 4:
                print("\033[0;36;40;1m■ \033[0m", end='')
            elif game_map[i][j] == 5:
                print("\033[0;32;40;1m■ \033[0m", end='')
        print()
    time.sleep(0.5)
    return


def get_children(current, game_map, last):
    children = []
    temp_children = [[current[0] + 1, current[1]], [current[0], current[1] + 1],
                     [current[0] - 1, current[1]], [current[0], current[1] - 1]]
    path = get_path(current, last)
    for child in temp_children:
        if game_map[child[0]][child[1]] and child not in path:
            children.append(tuple(child))
    return children


def get_path(current, last):
    path = [current]
    while last[current] != current:
        current = last[current]
        path.append(current)
    path.append(last[current])
    return path


def h_cost(child, goal):
    [x1, y1] = child
    [x2, y2] = goal
    return abs(x1 - x2) + abs(y1 - y2)


def Astar(game_map, start, goal):
    open_list = PriorityQueue()
    close_list = []
    visited = {}
    last = {}

    open_list.add(start, 0)
    last[start] = start
    visited[start] = 0

    while open_list.index:
        current = open_list.pop()
        if current != start:
            game_map[current[0]][current[1]] = 4
        close_list.append(current)
        if current == goal:
            # print(get_path(goal, last))
            return
        else:
            for child in get_children(current, game_map, last):
                g_cost = visited[current] + 1
                if child not in visited or g_cost < visited[child]:
                    child_cost = g_cost + h_cost(child, goal)
                    visited[child] = g_cost
                    open_list.add(child, child_cost)
                    last[child] = current
                    if child != goal:
                        game_map[child[0]][child[1]] = 5
            draw_map(game_map)
    print('查询失败，不能找到路径！')
    return

