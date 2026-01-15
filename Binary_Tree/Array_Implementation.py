# Binary Tree class is responsible for creating binary trees.
class ArrayBinaryTree:
    def __init__(self):
        self.tree = []
 # Insertion operation which has the time complexity of O(1) and space complexity of O(1)
    def insert(self, element):
        self.tree.append(element)
        print(f"{element} inserted.")
 
# Deletion operation which has the time complexity of O(n) and space complexity of O(1)
    def delete(self, element):
        if not self.tree:
            print("Tree is empty.")
            return

        if element not in self.tree:
            print("Element not found.")
            return

        index = self.tree.index(element)
        last_element = self.tree.pop()

        if index < len(self.tree):
            self.tree[index] = last_element
        print(f"{element} deleted.")

 # Traversal(BFS) operation which has the time complexity of O(n) and space complexity of O(1)
    def level_order(self):
        if not self.tree:
            print("Tree is empty.")
            return

        for ele in self.tree:
            print(ele, end=" ")
        print()


bt=ArrayBinaryTree()
while (True):
    print("Menu\n1.insert\n2.deletion\n3.Display(level order)\n4.exit")
    choice=input("Enter the valid choice number :")
    match choice:
        case '1':
            element=int(input("Enter the element to be inserted :"))
            bt.insert(element )
        case '2':
            element=int(input("Enter the element to be deleted :"))
            bt.delete(element )
        case '3':
            bt.level_order( )
        case '4':
            break
        case _:
            print("Invalid choice........")
