class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        
        # Map value → index in inorder for O(1) lookup
        idx = {v: i for i, v in enumerate(inorder)}
        
        def build(l, r):
            if l > r:
                return None
            
            # Last element in postorder is the root
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # In inorder, elements right of root_val belong to right subtree
            mid = idx[root_val]
            
            # Build right subtree *before* left because of postorder pop()
            root.right = build(mid + 1, r)
            root.left = build(l, mid - 1)
            
            return root
        
        return build(0, len(inorder) - 1)
