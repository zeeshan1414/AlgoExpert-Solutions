class BST:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    # O(log(n)) time | O(1) space
    def insert(self, val):
        currNode = self

        while True:
            if val < currNode.val:
                if currNode.left is None:
                    currNode.left = BST(val)
                    break
                else:
                    currNode = currNode.left
            else:
                if currNode.right is None:
                    currNode.right = BST(val)
                    break
                else:
                    currNode = currNode.right
        return self

    # O(log(n)) time | O(1) space
    def contains(self, val):
        currNode = self

        while currNode is not None:
            if val == currNode.val:
                return True
            elif val < currNode.val:
                currNode = currNode.left
            else:
                currNode = currNode.right

        return False

    def remove(self, val, parentNode=None):
        currNode = self

        while currNode is not None:
            if val < currNode.val:
                parentNode = currNode
                currNode = currNode.left
            elif val > currNode.val:
                parentNode = currNode
                currNode = currNode.right
            else:
                if currNode.left is not None and currNode.right is not None:
                    currNode.val = currNode.right.getMinValue()
                    currNode.right.remove(currNode.val, currNode)

                elif parentNode is None:
                    if currNode.left is not None:
                        currNode.val = currNode.left.val
                        currNode.right = currNode.left.right
                        currNode.left = currNode.left.left

                    elif currNode.right is not None:
                        currNode.val = currNode.right.val
                        currNode.left = currNode.right.left
                        currNode.right = currNode.right.right

                    else:
                        currNode.val = None

                elif parentNode.left == currNode:
                    parentNode.left = (
                        currNode.left if currNode.left is not None else currNode.right
                    )

                elif parentNode.right == currNode:
                    parentNode.right = (
                        currNode.left if currNode.left is not None else currNode.right
                    )
                break
        return self

    def getMinValue(self):
        currNode = self
        while currNode.left is not None:
            currNode = currNode.left
        return currNode.val

    def printBST(self, node):
        if node is None:
            return
        self.printBST(node.left)
        print(node.val, end=" ")
        self.printBST(node.right)


if __name__ == "__main__":
    bst = BST(10)
    bst.insert(12)
    bst.insert(13)
    bst.insert(15)
    bst.insert(4)
    print(bst.contains(12))
    bst.remove(4)
    bst.printBST(bst)
