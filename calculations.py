from typing import List
from cluster import Cluster


def distanceBetween(cluster_a: Cluster, cluster_b: Cluster) -> int:
    distance = 0
    for number in cluster_a.numbers:
        for check in cluster_b.numbers:
            if abs(number - check) > distance:
                distance = abs(number - check)
    return distance
