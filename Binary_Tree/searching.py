# Searching a element in binary tree which has the time complexity of O(n) and space complexity of O(H)
class operation:
    def search(self, root,element):
        if(root is None):
            return None
        if(root.data ==element):
            return root
        left=self.search(root.left, element)
        if(left):
            return left
        right=self.search(root.right, element)
        if(right):
            return right
        return None
   