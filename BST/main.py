from MyBST import BSTree

if __name__ =="__main__":
    tree = BSTree()

    tree.insert(8)
    tree.insert(10)
    tree.insert(14)
    tree.insert(13)
    tree.insert(3)
    tree.insert(6)
    tree.insert(14)
    tree.insert(1)
    tree.insert(4)
    tree.insert(7)
    tree.insert(2)

    tree.pre_order(tree.root)
    print()
    tree.in_order(tree.root)
    print()
    tree.post_order(tree.root)
    print()
    tree.breadth()
    print()
    found = tree.searchNodeHavingOnlyLeftChildByPreOrder(tree.root)
    if found != None:
        print(found.info)
    else:
        print("Not found")
