'''
3 scenarios

node is leaf -> simply delete

node has a single child, put child val into node, delete child

node had 2 children, take inorder successor(righ one and leftmost node), put that into node and delete the sucessor
O(h) normal, O(n) skewed

'''
