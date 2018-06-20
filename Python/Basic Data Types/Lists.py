if __name__ == '__main__':
    N = int(input())
    listCmd = []
    listVal = []
    for i in range(N):
        listCmd.append(input())
    for i in listCmd:
        line = i.split()
        cmd, placeval = line[0], line[1:]
        
        if(cmd == "insert"):
            listVal.insert(int(placeval[0]), int(placeval[1]))
        elif(cmd == "print"):
            print(listVal)
        elif(cmd == "remove"):
            listVal.remove(int(placeval[0]))
        elif(cmd == "sort"):
            listVal.sort()
        elif(cmd == "append"):
            listVal.append(int(placeval[0]))
        elif(cmd == "pop"):
            listVal.pop()
        elif(cmd == "reverse"):
            listVal.reverse()
            
    # print(listVal)
    
