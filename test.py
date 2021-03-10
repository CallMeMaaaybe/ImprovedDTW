from trendypy.trendy import Trendy
import numpy as np

if __name__ == '__main__':
    train = np.genfromtxt('Symbols_TRAIN.tsv', delimiter='\t')
    label = train[:, 0]
    train = train[:, 1:-1]
    # train = []
    # tem0 = [1,2,3,4,5,6,7,6,5,4,3,2] * 3
    # train.append(tem0)
    # tem1 = [i + 100 for i in tem0]
    # train.append(tem1)
    # tem2 = [1] * 36
    # tem3 = [100] * 36
    # train.append(tem2)
    # train.append(tem3)
    trendy = Trendy(n_clusters=6)
    trendy.fit(train)
    print(trendy.labels_)
    print(label)