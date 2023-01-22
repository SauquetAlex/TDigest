from tdigest import TDigest
import numpy as np
from numpy.random import random
from matplotlib import pyplot as plt


digest = TDigest()
plt.title("TDigest")

array = []

for x in range(5000):
    x = random()
    y = (x) ** 2
    array.append((x, y))
    digest.update(x, y)
# another_digest = TDigest()
# another_digest.batch_update(random(5000))
# print(another_digest.percentile(15))
# print(digest.percentile(15))
# sum_digest = digest + another_digest
# print(sum_digest.percentile(15))
centroids = []

for data in digest.to_dict()["centroids"]:
    centroids.append((data["m"], data["c"]))

# plt.hist(array, 50, facecolor='#265691')
# plt.axis([0, 1, 0, 1000])
# plt.show()

plt.scatter(*zip(*array), color='#265691')
plt.scatter(*zip(*centroids), color='#880808')
plt.axis([0, 1, 0, 1])
plt.show()
