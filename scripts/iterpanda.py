from sklearn.neighbors import DistanceMetric
import pandas as pd

dist = DistanceMetric.get_metric("haversine")

filename = "/Users/cosmos/Documents/dockerapp/STRAT\ETH 48960.csv"
array = pd.read_csv(str(filename))

print(array)
