q1>class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def convert_binary_tree_to_bst(root):
    # Step 1: Traverse the binary tree and store node values in a list
    def traverse(node, nodes_list):
        if node is None:
            return
        nodes_list.append(node.val)
        traverse(node.left, nodes_list)
        traverse(node.right, nodes_list)

    nodes = []
    traverse(root, nodes)

    # Step 2: Sort the list in ascending order
    nodes.sort()

    # Step 3: Traverse the binary tree again and replace node values with sorted values
    def replace_values(node, nodes_list):
        if node is None:
            return
        replace_values(node.left, nodes_list)
        node.val = nodes_list.pop(0)
        replace_values(node.right, nodes_list)

    replace_values(root, nodes)

    return root




q2>class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def construct_bst(values):
    root = None
    for val in values:
        root = insert_into_bst(root, val)
    return root


def insert_into_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root


def find_distance_between_nodes(root, node1, node2):
    # Step 1: Find the Lowest Common Ancestor (LCA)
    lca = find_lca(root, node1, node2)

    # Step 2: Calculate the distance from the LCA to both nodes
    dist1 = find_distance_from_node(lca, node1)
    dist2 = find_distance_from_node(lca, node2)

    # Step 3: Add the distances to get the total distance
    total_distance = dist1 + dist2

    return total_distance


def find_lca(root, node1, node2):
    if root is None or root.val == node1 or root.val == node2:
        return root

    if node1 < root.val and node2 < root.val:
        return find_lca(root.left, node1, node2)

    if node1 > root.val and node2 > root.val:
        return find_lca(root.right, node1, node2)

    return root


def find_distance_from_node(node, target):
    if node.val == target:
        return 0
    elif target < node.val:
        return 1 + find_distance_from_node(node.left, target)
    else:
        return 1 + find_distance_from_node(node.right, target)


# Example usage
values = [8, 3, 1, 6, 4, 7, 10, 14, 13]
root = construct_bst(values)

node1 = 6
node2 = 14

distance = find_distance_between_nodes(root, node1, node2)
print("The distance between the two keys =", distance)




q3>class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def convert_binary_tree_to_dll(root):
    def inorder_traversal(node):
        nonlocal prev, head

        if node is None:
            return

        inorder_traversal(node.left)

        if prev is None:
            # If prev is None, this is the leftmost node (head of the doubly linked list)
            head = node
        else:
            # Modify the pointers to create the doubly linked list
            prev.right = node
            node.left = prev

        prev = node

        inorder_traversal(node.right)

    # Special case for an empty tree
    if root is None:
        return None

    # Initialize variables
    prev = None
    head = None

    # Perform inorder traversal to convert the binary tree to a doubly linked list
    inorder_traversal(root)

    # Adjust the last node's pointers to complete the circular doubly linked list
    prev.right = None
    head.left = None

    return head


# Example usage
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

dll_head = convert_binary_tree_to_dll(root)

# Print the doubly linked list
current = dll_head
while current is not None:
    print(current.val, end=" ")
    current = current.right




q4>class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None


def connect_nodes_at_same_level(root):
    if root is None:
        return None

    # Start with the root node
    queue = [root]

    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)

        for i in range(level_size):
            # Pop the front node from the queue
            node = queue.pop(0)

            # Connect the current node to the next node in the queue
            if i < level_size - 1:
                node.next = queue[0]

            # Add the left and right child nodes to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return root


# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

connected_root = connect_nodes_at_same_level(root)

# Print the connected nodes
current = connected_root
while current:
    print(current.val, end=" → ")
    current = current.next
print("-1")
