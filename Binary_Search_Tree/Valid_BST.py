# Validation of Binary Search Tree by using recursion which has the time complexity of O(n) and space complexity of O(n)
class operations:
    def bst_validation(self,root, mini, maxi): 
        if(root==None):
            return True 
        
        if(mini< root.data and maxi> root.data):
            left=self.retry(root.left,mini,root.data)
            right=self.retry(root.right,root.data,maxi)
            return left and right
        else:
            return False 