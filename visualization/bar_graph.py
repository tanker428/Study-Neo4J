import numpy as np
import matplotlib.pyplot as plt

"""
グラフの表示方法
このファイルを実行する場合、このファイル上で右クリック
pythonの実行 > ターミナルでpythonを実行を選択
"""

 
left = np.array([1, 2, 3, 4, 5])
height = np.array([100, 200, 300, 400, 500])
plt.bar(left, height)
plt.show()