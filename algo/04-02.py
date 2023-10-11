## 함수 
class  Node() : 
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None) :
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre
    # Case 1 : 머리앞에 삽입 (다현화사)
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node 
        memory.append(node) # 생략가능 
        return
    # Case 2 : 중간 노드 앞에 삽입(사나솔라)
    current = head 
    while (current.link != None):
        pre = current 
        current = current.link
        if (current.data == findData):
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    node = Node()
    node.data = insertData
    current.link = node 
    return
    


def deleteNode(deleteData):
    global memory, head, current, pre 
    # 머리삭제
    if (head.data == deleteData):
        current = head 
        head = head.link
        del(current)
        return
    # 중간노드 삭제
    current = head 
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == deleteData):    
            pre.link = current.link
            del(current)
            return
    

        
def findNode(findData):
    global memory, head, current, pre 
    current = head 
    if (current.data == findData):
        return current
    
    while (current.link != None):
        current = current.link
        if (current.data == findData):
            return current
    return Node()




## 전역 
memory = []
head, current, pre = None, None, None
dataArray = ['다현', ' 정연', '쯔위', '사나', '지효']

## 메인

node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 파이썬은 생략가능 

node2 = Node()

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node) # 파이썬은 생략가능 

printNodes(head)


# insertNode('다현','화사')
# printNodes(head)
# insertNode('사나', '솔라')
# printNodes(head)
# insertNode('현정', '문별')
# printNodes(head)

# deleteNode('다현')
# printNodes(head)
# deleteNode('쯔위')
# printNodes(head)


retData = findNode('사나')
printNodes(retData.data, '가 플레이 됩니다~')