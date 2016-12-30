class TreeNode:
    def __init__(self,val):
        self.val  = val
        self.left = None
        self.right = None


def createTree123():
    # root = TreeNode(8)
    # root.right = TreeNode(10)
    # root.left = TreeNode(3)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(6)
    # root.left.right.left = TreeNode(4)
    # root.left.right.right = TreeNode(7)
    # root.right.right = TreeNode(14)
    # root.right.right.left = TreeNode(13)
    # root = TreeNode(8)
    # root.right = TreeNode(10)
    root = TreeNode(0)
    root.left = TreeNode(1)

    return root

def inorderRecursive(root):
    if not root:
        return
    inorderRecursive(root.left)
    print root.val,
    inorderRecursive(root.right)

def inorderMorris(root):
    current = root
    switched = [None,None]
    prev = None
    while current:
        if not current.left:
            print current.val,prev
            prev = current.val
            current = current.right

        else:
            pred = current.left
            while pred.right!=current and pred.right:
                pred=pred.right
            if not pred.right:
                pred.right = current
                current = current.left
            else:
                pred.right = None
                print current.val,prev
                prev = current.val
                current=current.right

def inorderMorris2(root,switched):
            prev=None

            while root:
                if not root.left:
                    if prev and prev.val>root.val:
                        if not switched:
                            switched.append(prev)
                            switched.append(root)
                        else:
                            switched[1] = root

                    prev = root
                    print root.val,
                    root = root.right
                else:
                    pred = root.left
                    while pred.right!=root and pred.right:
                        pred=pred.right
                    if not pred.right:
                        pred.right = root
                        root = root.left
                    else:
                        pred.right = None
                        prev = root
                        if prev and prev.val>root.val:
                            if not switched:
                                switched.append(prev)
                                switched.append(root)
                            else:
                                switched[1] = root

                        print root.val,
                        root = root.right

if __name__ == "__main__":
    root = createTree123()
    #inorderRecursive(root)
    swap = []
    inorderMorris2(root,swap)
    print "len of swap = "
    for i in swap:
        print i.val
