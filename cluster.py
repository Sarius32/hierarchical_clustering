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
