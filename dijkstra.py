def createNewDict(prevDist, prevName = "", num = -1, data = []):
    global spt, lowestNode, splitString
    dict = {}
    if prevName == "":
        prevName = input("File Name (or hit enter): ")
        data = open(f"{prevName}.txt", "r").read().splitlines()
        num = int(len(data))
    elif num == -1:
        num = int(input("Number of Nodes: "))
    for i in range(num):
        if prevName == "":
            name = input(f"Node {i+1} name: ")
            dist = int(input(f"Node {i+1} value: ")) + prevDist
        else:
            name = data[i].split(splitString)[0]
            dist = int(data[i].split(splitString)[1])+prevDist
        if name not in spt and dist < stopNum:
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
        
def updateNode(dict, args):
    global spt, lowestNode, recentMinNum
    spt[lowestNode[0]] = lowestNode[1]
    recentMinNum = lowestNode[1]
    #print(f"Define nodes for {lowestNode[0]}: ")
    if len(args) == 0:
        dict[lowestNode[0]][1] = createNewDict(lowestNode[1])
    else:
        dict[lowestNode[0]][1] = createNewDict(lowestNode[1], args[0], args[1], args[2])
    #print(dict[lowestNode[0]][1])
    lowestNode = ("", stopNum)

def updateMinNode(dict, args = []):
    global spt, lowestNode, path
    for name, arr in dict.items():
        if(name == lowestNode[0] and arr[0] == lowestNode[1]):
            path.append(name)
            #print(path)
            updateNode(dict, args)
            break
        elif(lowestNode[0] == ""):
            break
        elif(arr[1] != {}):
            path.append(name)
            updateMinNode(arr[1], args)
            if(lowestNode[0] != ""):
                path.pop()
def reset(FROM_COMMAND_LINE = False):
    global spt, recentMinNum, lowestNode, initialNode
    spt = {}
    recentMinNum = 0
    lowestNode = ("", stopNum)
    if FROM_COMMAND_LINE:
        initialNode = createNewDict(0) 
    else:
        initialNode = {}

spt = {}        # Shortest Path Tree
recentMinNum = 0        # Holds the most recent lowest node's value
path = []       # Hold the path to the current lowest node
splitString = " in "        # String that splits the node names and node values in a text file
stopNum = 97        # Max distance a node can be from the starting node before the program stops
lowestNode = ("", stopNum)       # Tuple to hold the lowest node of all currently known nodes
initialNode = {}     # The initial node


# This is how to run the algorithm
# reset()
# while(recentMinNum < stopNum):
#     findMinNode(initialNode)
#     updateMinNode(initialNode)
#     path = []
#     print(spt)
