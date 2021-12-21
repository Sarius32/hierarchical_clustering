from cluster import Cluster
from io_utils import printCurrentClusters, printStartClusters


points = [1, 4, 9, 25, 16, 32, 63, 81, 100, 121, 144]
points.sort()


def main() -> None:
    step = 1

    clusters = []
    for point in points:
        clusters.append(Cluster(point))

    printStartClusters(clusters)

    max_distance = abs(points[0] - points[-1])
    while(len(clusters) > 2):
        distances = []
        for a in range(len(clusters)):
            min_distance = (0, max_distance)
            for b in range(len(clusters)):
                if a == b:
                    continue

                dis = clusters[a].calcDistance(clusters[b])
                if dis < min_distance[1]:
                    min_distance = (b, dis)
            
            distances.append(min_distance)
        
        joining = (0, 0, max_distance)
        for i in range(len(distances)):
            if distances[i][1] < joining[2]:
                joining = (i, *distances[i])

        clusters[joining[0]].addCluster(clusters[joining[1]])
        clusters.pop(joining[1])

        printCurrentClusters(step, joining[0], clusters)
        step += 1


    clusters[0].addCluster(clusters[1])
    clusters.pop()

    printCurrentClusters(step, 0, clusters)

main()
