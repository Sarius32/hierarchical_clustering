points = [1, 4, 9, 16, 25, 32, 63, 81, 100, 121, 144]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Cluster:
    def __init__(self, number: int) -> None:
        self.numbers = [number]

    def addCluster(self, cluster) -> None:
        self.numbers.extend(cluster.numbers)

    def calcDistance(self, cluster) -> None:
        distance = 0
        for number in self.numbers:
            for check in cluster.numbers:
                if abs(number - check) > distance:
                    distance = abs(number - check)
        return distance
    
    def __str__(self) -> str:
        return str(self.numbers)


def main() -> None:
    print()
    step = 1

    clusters = []
    for point in points:
        clusters.append(Cluster(point))

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

        output = f"{step}. Step: "
        for i in range(len(clusters)):
            if i == joining[0]:
                output += f"{bcolors.FAIL}{clusters[i]}{bcolors.ENDC}"
            else:
                output += str(clusters[i])
            if i != len(clusters)-1:
                output += ", "
        print(output, end="\n\n")

        step += 1


    clusters[0].addCluster(clusters[1])
    clusters.pop()

    print(f"{step}. Step: {bcolors.FAIL}{bcolors.UNDERLINE}{clusters[0]}{bcolors.ENDC}", end="\n\n")

main()
