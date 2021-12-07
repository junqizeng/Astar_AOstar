import time
import os


def get_node(mark_road, extended):
    temp = [0]
    i = 0
    while 1:
        current = temp[i]
        if current not in extended:  # 找到没有被扩展过的结点
            return current
        else:
            for child in mark_road[current]:  # 如果当前结点被扩展过，那么采用dfs的思想，把其标志路的子代加入
                if child not in temp:
                    temp.append(child)
            i += 1


def get_current(S, nodes_tree):
    if len(S) == 1:
        return S[0]
    for node in S:
        flag = True
        for edge in nodes_tree(node):
            for child_node in edge:
                if child_node in S:
                    flag = False
        if flag:
            return node


def get_pre(current, pre, pre_list):
    if current == 0:
        return
    for pre_node in pre[current]:
        if pre_node not in pre_list:
            pre_list.append(pre_node)
        get_pre(pre_node, pre, pre_list)
    return


def ans_print(mark_rode, node_tree):
    print("最终连接情况如下：")
    temp = [0]
    while temp:
        time.sleep(1)
        print(f"[{temp[0]}] ------> {mark_rode[temp[0]]}")
        for child in mark_rode[temp[0]]:
            if node_tree[child] != [[child]]:
                temp.append(child)
        temp.pop(0)
    time.sleep(5)
    os.system('cls')
    return


def AOstar(nodes_tree, h_val):
    futility = 0xfff
    extended = []
    choice = []
    mark_rode = {0: None}
    solved = {}
    pre = {0: []}
    ans_process = []
    for i in range(1, 9):
        pre[i] = []
    for i in range(len(nodes_tree)):  # 将所有的结点设置为非solved
        solved[i] = False
    # os.system('cls')
    # print("连接过程如下")
    # time.sleep(1)
    while not solved[0] and h_val[0] < futility:  # 当初始结点非solved且未超过阈值时
        node = get_node(mark_rode, extended)   # 找到标志路上未扩展的一个结点
        extended.append(node)
        if nodes_tree[node] is None:  # 如果找到的node没有后继，
            h_val[node] = futility
            continue
        for suc_edge in nodes_tree[node]:  # 生成node的后继结点
            for suc_node in suc_edge:
                if nodes_tree[suc_node] == [[suc_node]]:  # 如果属于解，则标志为solved
                    solved[suc_node] = True
        S = [node]
        while S:  # 当S不为空时
            current = get_current(S, nodes_tree)  # 找到后继节点不在S中的current
            S.remove(current)
            origen_h = h_val[current]
            origen_s = solved[current]

            min_h = 0xfff
            for edge in nodes_tree[current]:  # 遍历出current最短子路径
                edge_h = 0
                for node in edge:
                    edge_h += h_val[node] + 1   # 子结点的花费 + 路径1费
                if edge_h < min_h:
                    min_h = edge_h
                    h_val[current] = min_h
                    mark_rode[current] = edge
            if mark_rode[current] not in choice:
                choice.append(mark_rode[current])
                ans_process.append([current, mark_rode[current]])
                # print(f"[{current}] ------> {mark_rode[current]}")
                # time.sleep(1)
            for child_node in mark_rode[current]:  # 子路径中的每个结点前驱设为current
                pre[child_node].append(current)
            solved[current] = True  # 如果子路径的每个结点都是solved，那么current也被设置为solved
            for node in mark_rode[current]:
                solved[current] = solved[current] and solved[node]
            if origen_s != solved[current] or origen_h != h_val[current]:
                pre_list = []
                if current != 0:  # 如果是0结点发生了改动，那么不需要再把0结点作为自己的前驱再加入S
                    get_pre(current, pre, pre_list)
                S.extend(pre_list)
    if not solved[0]:
        print("查询失败，不能找到路径！")
        return False, None
    else:
        # ans_print(mark_rode, nodes_tree)
        return True, ans_process
