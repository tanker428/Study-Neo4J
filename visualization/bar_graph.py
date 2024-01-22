import numpy as np
import matplotlib.pyplot as plt

"""
グラフの表示方法
このファイルを実行する場合、このファイル上で右クリック
pythonの実行 > ターミナルでpythonを実行を選択
"""


# 例
# score_dict = {"Pottery": 32, "Crate": 2, "Dog": 109}
# score_sorted_dict = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)

# print(score_sorted_dict)

def bar_graph(dict):
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
    plt.show()    
    
    return

# bar_graph({"Pottery": 32, "Crate": 2, "Dog": 109})