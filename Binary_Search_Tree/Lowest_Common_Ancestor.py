# Lowest Common Ancestor which has the time complexity of O(n) and space complexity of O(n)
class Operation: 
    def lca(self, root,p,q):
        if(root==None):
            return None
        if(root.data>p and root.data>q):
           return self.lca(root.left,p,q)
        elif(root.data<p and root.data<q):
            return self.lca(root.right,p,q)
        else :
            return root