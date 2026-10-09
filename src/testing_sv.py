import yaml
from src.data import load_data
from src.kmeans import KMeansScratch, KMeansReference

cfg = yaml.safe_load(open('config.yaml'))
data = load_data(cfg)
X = [data['array1'], data['array2'], data['list1'], data['list2']]  # the standardized (3730, 39) array from `data`

for k in range(2, 16):
    s = KMeansScratch(k=k, n_init=30, seed=42).fit(X)
    r = KMeansReference(k=k, n_init=30, seed=42).fit(X)
    print(k, round(s.inertia_), round(r.inertia_), round(s.inertia_ / r.inertia_, 3))