# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # As per the reference given in the description, Leetcode, serializes the binary tree using level order traversal but we don't have to follow the same traversal style, for our convenience, we will use recursive preorder traversal.

        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return 
            res.append(str(node.val)) # node.val is usually an integer, and if we don't convert it to the string then the result will have a mix of string and integer, while using "join" at the end, there'd be an error indicating the same.
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # To deserialize the tree, firstly we need to convert this back to the integer, also, we need to use TreeNode object to indicate that we are converting this string array back to the tree.

        vals = data.split(",")
        self.i = 0 # We have to use self because we are using the same paratmeter given to us by the code to specify which pointer of data we are at right now.

        # We will run the dfs again, but this time on the vals array and convert them one by one to the treenode.

        def dfs(): # You don't have to pass any parameter because the next node to be processed is determined by the self.i, which is determined in the definition. We don't have an already present node in deserialize because there is no tree right now, there is just an array os strings.
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))