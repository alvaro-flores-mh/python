from typing import List, Dict
from collections import Counter
import math
import matplotlib.pyplot as plt
import time
def bucketize(point: float, bucket_size: float) -> float:
    return bucket_size * math.floor(point / bucket_size)

def make_histogram(points: List[float], bucket_size: float) -> Dict[float,int]:
    return Counter(bucketize(point, bucket_size) for point in points)

def plot_histogram(points: List[float], bucket_size:float, title: str = ""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width= bucket_size)
    plt.title(title)
    plt.show()
    #time.sleep(10)
    
    
import random

from scratch.probability import inverse_normal_cdf

random.seed(0)

#uniforme entre -100 y 100
uniform = [200 * random.random()-100 for _ in range(10000)]

normal = [57 * inverse_normal_cdf(random.random())
          for _ in range(10000)]

plot_histogram(uniform, 10, "Uniform Histogram")

plot_histogram(normal, 10, "Normal Histogram")

def random_normal() -> float:
    
    return inverse_normal_cdf(random.random())

xs = [random_normal() for _ in range(1000)]
ys1 = [ x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]


plt.scatter(xs, ys1, marker='.', color="black", label='ys1')
plt.scatter(xs, ys2, marker='.', color="gray", label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("Muy diferente distribuciones")
plt.show()