from typing import List
from cluster import Cluster


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


def printStartClusters(clusters: List[Cluster]) -> None:
    print("\nStart: " + ", ".join(map(showAsCluster, clusters)) + "\n")

def printCurrentClusters(current_step: int, joined_position: int, clusters: List[Cluster]) -> None:
    output = f"{current_step}. Step: "
    for i in range(len(clusters)):
        if i == joined_position:
            output += bcolors.FAIL + showAsCluster(clusters[i]) + bcolors.ENDC
        else:
            output += showAsCluster(clusters[i])
        if i != len(clusters)-1:
            output += "; "
    print(output, end="\n\n")

def showAsCluster(cluster: Cluster) -> str:
    return "{" + ", ".join(map(str, cluster.numbers)) + "}"
    