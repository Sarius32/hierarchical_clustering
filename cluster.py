class Cluster:
    def __init__(self, number: int) -> None:
        self.numbers = [number]

    def addCluster(self, cluster) -> None:
        self.numbers.extend(cluster.numbers)
    
    def __str__(self) -> str:
        return str(self.numbers)
