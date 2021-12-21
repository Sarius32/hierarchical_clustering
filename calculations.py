from typing import List
from cluster import Cluster


def distanceBetween(cluster_a: Cluster, cluster_b: Cluster) -> int:
    distance = 0
    for number in cluster_a.numbers:
        for check in cluster_b.numbers:
            if abs(number - check) > distance:
                distance = abs(number - check)
    return distance


def maxDistance(clusters: List[Cluster]) -> int:
    distance: int
    for index_a, cluster_a in enumerate(clusters):
        for index_b, cluster_b in enumerate(clusters):
            if index_a == index_b:
                continue
            elif index_a == 0 and index_b:
                distance = distanceBetween(cluster_a, cluster_b)
            else:
                dis = distanceBetween(cluster_a, cluster_b)
                if dis > distance:
                    distance = dis
    
    return distance