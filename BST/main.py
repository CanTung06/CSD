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

    # tree.pre_order(tree.root)
    # print()
    # tree.in_order(tree.root)
    # print()
    # tree.post_order(tree.root)
    # print()
    # tree.breadth()
    # print()
    # found = tree.searchNodeHavingOnlyLeftChildByPreOrder(tree.root)
    # if found != None:
    #     print(found.info)
    # else:
    #     print("Not found")

    tree.insert(12)
    tree.delete(14)
    tree.delete(10)

    tree.insert(30)
    tree.insert(25)
    tree.insert(35)
    tree.insert(23)
    tree.insert(26)
    tree.insert(22)
    tree.insert(24)
    tree.insert(29)
    tree.insert(28)
    tree.insert(27)

    tree.delete(30)
    tree.breadth()
    print()
    tree.insert(0)
    tree.delete(3)

    tree.delete_by_merging(29)
    tree.delete_by_merging(8)
    tree.rotate_right(25)
    tree.rotate_right(1)
    tree.breadth()

    