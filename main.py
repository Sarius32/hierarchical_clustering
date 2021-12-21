from typing import List
from calculations import distanceBetween, maxDistance
from cluster import Cluster
from io_utils import printCurrentClusters, printEndCluster, printStartClusters


def main(clusters: List[Cluster]) -> None:
    step = 0
    printStartClusters(clusters)

    while(len(clusters) > 2):
        step += 1
        join: tuple[int, int, int]
        for index_a, cluster_a in enumerate(clusters):
            for index_b, cluster_b in enumerate(clusters):
                if index_a == 0 and index_b == 1:
                    join = (index_a, index_b, distanceBetween(cluster_a, cluster_b))
                elif index_a != index_b:
                    dis = distanceBetween(cluster_a, cluster_b)
                    if join[2] > dis:
                        join = (index_a, index_b, distanceBetween(cluster_a, cluster_b))

        clusters[join[0]].addCluster(clusters[join[1]])
        clusters.pop(join[1])

        printCurrentClusters(step, join[0], clusters)
        

    step += 1
    clusters[0].addCluster(clusters[1])
    clusters.pop()

    printEndCluster(clusters)


if __name__ == "__main__":
    points = [1, 4, 9, 25, 16, 32, 63, 81, 100, 121, 144]
    points.sort()

    clusters = []
    for point in points:
        clusters.append(Cluster(point))

    main(clusters)
