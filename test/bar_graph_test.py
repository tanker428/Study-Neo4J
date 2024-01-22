import numpy as np
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from visualization.bar_graph import bar_graph

"""
グラフの表示方法
このファイルを実行する場合、このファイル上で右クリック
pythonの実行 > ターミナルでpythonを実行を選択
"""

# 参考記事　https://www.yutaka-note.com/entry/matplotlib_bar#%E5%9F%BA%E6%9C%AC%E7%9A%84%E3%81%AA%E6%A3%92%E3%82%B0%E3%83%A9%E3%83%95%E3%81%AE%E4%BD%9C%E6%88%90pltbar

# 例
score_dict = {"Pottery": 32, "Crate": 2, "Dog": 109}
labels = ["a", "b", "c", "d", "e"]
score_sorted_dict = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)
number = len(score_dict)
print(number)
print(score_sorted_dict)
#この辞書for文で

 # ここに下の名称を入れる x軸　ex Pottery
left = np.array([1, 2, 3, 4, 5])

# ここに数値を入れる y軸 ex 32
height = np.array([100, 200, 300, 400, 500])
# plt.bar(left, height, tick_label=labels)
# plt.show()

bar_graph(score_dict)
