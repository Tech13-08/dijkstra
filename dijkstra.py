def createNewDict(prevDist):
    global spt, lowestNode, splitString
    dict = {}
    prevName = input("File Name (or hit enter): ")
    data = []
    num = 0
    if prevName != "":
        data = open(f"{prevName}.txt", "r").read().splitlines()
        num = int(len(data))
    else:
        num = int(input("Number of Nodes: "))
    for i in range(num):
        if prevName == "":
            name = input(f"Node {i+1} name: ")
            dist = int(input(f"Node {i+1} value: ")) + prevDist
        else:
            name = data[i].split(splitString)[0]
            dist = int(data[i].split(" in ")[1])+prevDist
        if name not in spt and dist < 97:
            if(name in dict):
                if dict[name][0] > dist:
                    dict[name] = [dist, {}]
            else:
                dict[name] = [dist, {}]
    
    return dict        

def findMinNode(dict):
    global spt, lowestNode
    for name, arr in dict.items():
        if(name not in spt and arr[0] < lowestNode[1]):
            lowestNode = (name, arr[0])
        if(arr[1] != {}):
            findMinNode(arr[1])
        
def updateNode(dict):
    global spt, lowestNode, recentMinNum
    spt[lowestNode[0]] = lowestNode[1]
    recentMinNum = lowestNode[1]
    print(f"Define nodes for {lowestNode[0]}: ")
    dict[lowestNode[0]][1] = createNewDict(lowestNode[1])
    print(dict[lowestNode[0]][1])
    lowestNode = ("", 97)

def updateMinNode(dict):
    global spt, lowestNode, path
    for name, arr in dict.items():
        if(name == lowestNode[0] and arr[0] == lowestNode[1]):
            path.append(name)
            print(path)
            updateNode(dict)
            break
        elif(lowestNode[0] == ""):
            break
        elif(arr[1] != {}):
            path.append(name)
            updateMinNode(arr[1])
            if(lowestNode[0] != ""):
                path.pop()

spt = {}        # Shortest Path Tree
recentMinNum = 0        # Holds the most recent lowest node's value
path = []       # Hold the path to the current lowest node
splitString = " in "        # String that splits the node names and node values in a text file
stopNum = 97        # Max distance a node can be from the starting node before the program stops
lowestNode = ("", stopNum)       # Tuple to hold the lowest node of all currently known nodes
initialNode = createNewDict(0)      # The initial node with a value of 0
while(recentMinNum < stopNum):
    findMinNode(initialNode)
    updateMinNode(initialNode)
    path = []
    print(spt)


