class Operation : 
    def __init__(self):
        self.count=0
    def kth(self,root,k): 
        if(root==None) :
            return None
        
        left=self.kth(root.left, k)
        if(left):
            return left
        self.count+=1
        if(self.count==k):
            return root.data
        right=self.kth(root.right,k)
        if(right):
            return right 