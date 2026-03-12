# Diameter of the btree which has the time complexity of O(n) and space complexity of O(n)
def final(self,btree):
        if(btree is None):
            return 0
        self.result=0
        def hight(tree):
            if(tree is None):
                return 0
            else:
                left=hight(tree.left)
                right=hight(tree.right)
                self.result=max(self.result,left+right)
            return (1+max(left,right))
        hight(btree)
        return self.result

        