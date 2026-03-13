# Deepest path finding by using recursion which has the time complexity of O(n) and space complexity of O(n)
class operation: 
    path=''
    def deepest_node(self,btree):
        if(btree is None):
             return 0,[]
        left,left_path=self.deepest_node(btree.left)
        right, right_path=self.deepest_node(btree.right)
        if(left>right):
            return 1+left, [btree.data]+left_path 
        else :
            return 1+right, [btree.data]+right_path