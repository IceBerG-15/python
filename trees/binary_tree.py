class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
# insert the node in the tree
def insert(root,val):
    if root == None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left,val)
    else:
        root.right = insert(root.right,val)
    return root
# inorder traversal
def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.val,end=' ')
    inorder(root.right)
# preorder traversal 
def preorder(root):
    if root == None:
        return
    print(root.val,end=' ')
    preorder(root.left)
    preorder(root.right)
# postorder traversal
def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=' ')

def main():
    root = None
    root = insert(root,10)
    root = insert(root,5)
    root = insert(root,15)
    root = insert(root,20)
    inorder(root)
    print()
    preorder(root)
    print()
    postorder(root)
    
if __name__ == "__main__":
    main()