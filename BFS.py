# 幅優先検索
"""
引数 : (tree, n):

返却値 : スコープIdの配列(ステートメントIdを要素番号、配列を要素にする)
"""
# https://qiita.com/takayg1/items/05d33193fbd7f2fc9256

from collections import deque


def search(u, n, g):
    queue = deque([u])
    d = [None] * n  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


def main(tree, n):
    print("BFS.pyのmain()を実行します。")
    print("tree", tree)
    # nは個数個のため調整。
    n += 1
    # 木は隣接リストに変換する。
    # n, m = [int(x) for x in input().split()] # nは頂点の数、mは辺の数
    g = [[] for _ in range(n)]  # 隣接リスト
    # 頂点の数も辺の数も「n」
    for key_num in tree.keys():
        # print("29：", key_num,tree)
        pairs = tree[key_num]
        for pair in pairs:
            g[key_num].append(pair)
            g[pair].append(key_num)
    print("BFS.pyのmain()を実行しました。")
    return search(0, n, g)


"""if __name__ == '__main__':
    n = 11
    dic_t = {0: [1, 2, 5, 7, 9], 2: [3, 4], 5: [6], 7: [8], 9: [10]}
    print(main(dic_t, n))"""


def search_new(dic_tree, start_id, time, return_list, adjust_num=1):
    # print("48", dic_tree, start_id, time, return_list)
    if start_id in dic_tree:
        children = dic_tree[start_id]
        # print(start_id, ">>", children)
        for child in children:
            return_list[child] = (time + adjust_num)
            search_new(dic_tree,  child, time+1, return_list)
    return return_list

# Noneなどが含まれている場合


def main_update(dic_tree, n):
    return_list = [0] + [None] * (n)
    print("BFS.pyのmain_update()を実行します。")
    print("65",dic_tree)
    start_id = 0
    time = 0
    return_list = search_new(dic_tree, start_id, time, return_list, 0)
    # children = dic_tree[]
    # nこの木がある時、最大の深さはn
    print("BFS.pyのmain_update()を実行しました。")
    print(return_list)
    return return_list


def update_list(parent, dic_tree, time, return_list):
    if parent in dic_tree:
        children = dic_tree[parent]
        for child in children:
            return_list[child] = time
            update_list(child, dic_tree, time+1, return_list)
    return return_list


def main_update2(dic_tree, n):
    return_list = [0] + [None] * (n)
    # print("BFS.pyのmain_update2()を実行します。")
    # 木を検索してBFSをする。
    # print("dic_tree", dic_tree)

    return_list = update_list(0, dic_tree, 0, return_list)

    # nこの木がある時、最大の深さはn
    # print("BFS.pyのmain_update2()を実行しました。")
    # print(return_list)
    return return_list


def main_update_mB(mB_source):
    # print(70, mB_source.sIds)
    length = len(mB_source.sIds)
    isIndent = False
    for i in range(length):
        obj = mB_source.dic_stats[i]
        # print(i, obj)
        s = obj[0]
        """if s == "":
            isIndent = True
            mB_source.sIds[i-1] -= 1"""
        """if isIndent:
            mB_source.sIds[i] -= 1"""

    return mB_source.sIds
