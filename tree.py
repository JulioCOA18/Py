class Node:
    def __init__(self,data):
        self.data = data
        self.sibling = None
        self.children = None
        
    
class Tree:
    def __init__(self):
        self.root = None
    
    def create(self,data):
        if(self.root is None):
            self.root = Node(data)
            return
        return print('The roo has not been created')
    
    def getRoot(self):
        
        if(self.root is not None):
            return self.root
        return print('You have to create a root')
    
    def append(self, data, wanted, root, kindred):

        if(root.data == wanted):

            if(root.data == wanted and kindred == True):
                self.appendSibling(data, root)
            else:
                self.appendSibling(data, root)

        if(root.sibling):
            self.append( data, wanted, root.sibling, kindred)
        
        if(root.children):
            self.append( data, wanted, root.children, kindred)

    def appendSibling(self,data,root):
        if(root.sibling):
            self.appendSibling(data,root.sibling)
        if(root.sibling is None):
            root.sibling = Node(data)

    def appendChildren(self,data,root):
        if(root.children is None):
            self.appendSibling(data,root.sibling)
        if(root.children is None):
            root.children = Node(data)
    
    def printTree(self,root):
        print(root.data)

        if(root.sibling is not None):
            self.printTree(root.sibling)
        if(root.children is not None):
            self.printTree(root.children)
    
tree = Tree()
tree.create(345)
root = tree.getRoot()
tree.append(34,345,root,False)
tree.append(256,345,root,True)
tree.printTree(root)