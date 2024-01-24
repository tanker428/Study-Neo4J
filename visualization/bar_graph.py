import numpy as np
import matplotlib.pyplot as plt

"""
グラフの表示方法
このファイルを実行する場合、このファイル上で右クリック
pythonの実行 > ターミナルでpythonを実行を選択
"""
# 参考記事　https://www.yutaka-note.com/entry/matplotlib_bar#%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E6%A3%92%E3%82%B0%E3%83%A9%E3%83%95%E3%81%AE%E4%BD%9C%E6%88%90pltbar
# https://www.yutaka-note.com/entry/matplotlib_axis#%E8%BB%B8%E3%83%A9%E3%83%99%E3%83%AB%E3%81%AE%E8%A1%A8%E7%A4%BA

# 例
# score_dict = {"Pottery": 32, "Crate": 2, "Dog": 109}
# score_sorted_dict = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)

# print(score_sorted_dict)

def bar_graph(dict, xlabel, ylabel):
    """
    例 このようなdictから棒グラフ作成
    score_dict = {"Pottery": 32, "Crate": 2, "Dog": 109}
    """
    sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    labels = []
    scores = []

    for k,v in sorted_dict:
        labels.append(k)
        scores.append(v)

    # print(labels, scores)

    height = np.array(scores)
    plt.bar(labels, height)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()    
    
    return

# bar_graph({"Pottery": 32, "Crate": 2, "Dog": 109})

def bar_graph_flame(dict):
    return