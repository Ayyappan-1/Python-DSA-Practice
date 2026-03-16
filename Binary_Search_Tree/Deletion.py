# BST deletion operation which has the time complexity of O(n) and O(n)

class operations :
    def deletion(self, element, root): 

        def find(element, root,parent):
            if(root is None):
                return  None,None
            if(root.data==element):
                 return root,parent
            elif(root.data>element):  
                 return find(element, root.left,root)
            else:  
                return find(element, root.right,root)  
            
        def inorder_successor( root,parent):
            if(root.left is None):
                return root, parent
            return inorder_successor(root.left,root)
        
            
        deletion,delete_parent = find(element, root, None)
        if(deletion is None):
            print("Invalid data, no value found")
            return
        # case 1 
        if(deletion.left is None and deletion.right is None):
            if(delete_parent==None):
                root=None
                return root

            if(delete_parent.left==deletion):
                delete_parent.left=None
            else:
                delete_parent.right=None 
            return
        # case 2
        if(deletion.left and deletion.right):
            inorder, inorder_parent=inorder_successor(deletion.right, deletion)
            deletion.data=inorder.data  
            if(inorder_parent==deletion or inorder==deletion.right):
                deletion.right=inorder.right
                return 
            else:  
                inorder_parent.left=inorder.right
        # case 3
        else:
            if(deletion.left):
                child=deletion.left
            else:
                child=deletion.right

            if(delete_parent is None):
                root=child
                return root
            
            if(delete_parent.left == deletion):
                delete_parent.left=child
            else:
                delete_parent.right=child

