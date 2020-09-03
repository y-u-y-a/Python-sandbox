from sklearn import datasets, svm
# 特徴量のデータ [0:男 1:女, 年齢]
feature = [
    [0, 28],
    [1, 20],
    [0, 32],
    [0, 67],
    [1, 8]
]
# 正解のデータ → 0:プログラマじゃない 1:プログラマ
job = [1, 0, 1, 0, 1]

# 予測させるデータ → 女２８歳
test_data = [[1, 28]]

# SVMというアルゴリズムを用いて学習
clf = svm.SVC(gamma = "scale") # インスタンス
clf.fit(feature, job) # 実際に学習させる
# 学習機械にデータを学習させる → fit()
# データを与えて予測させる    → predict()

# 三項演算子
print("プログラマ" if clf.predict(test_data)[0] else "プログラマじゃない")
