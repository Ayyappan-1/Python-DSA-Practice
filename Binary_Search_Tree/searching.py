# Searching a element in binary search tree by using recursion which has the time complexity of O(n) and Space complexity of O(n)
class operations:
    def search_recursion(self, root, element):
        if(root==None):
            return None
        if(element==root.data):
            return root
        elif(element>root.data):
            return self.search(root.right, element)
        else :
            return self.search(root.left,element)

# Searching a element in binary search tree normally without recursion which has the time complexity of O(n) and Space complexity of O(n)

    def basic_seraching(self,root,element):
        if(root==None):
            return None
        current=root
        while current:
            if(current.data==element):
                return current
            elif(current.data>element): 
                    current=current.leftn
            else:
                    current=current.right 
        return None
    
    search_recursion(root, element)
    basic_seraching(root,element)