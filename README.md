# User documentation

 The Binary Tree Visualizer is a graphical application for managing and visualizing binary trees. It allows users to add, remove, and clear nodes while providing an interactive view of the tree structure.

----------------------------------------------------------

### Getting Started
Launching the Application
1. Run the script in Python (e.g., type in terminal "python main.py" while being in the folder with the .py file).
2. The application window will open, showing two main sections:
- A left panel with controls and some statistics.
- A right panel where the binary tree is visualized.

----------------------------------------------------------

## How to Use the Application

### Adding a Node:
1. Type a numerical value into the Add Node input box.
2. Click the ADD button.
3. The new node will appear in the tree visualization.

### Removing a Node:
1. Type a numerical value into the Remove Node input box.
2. Click the DEL button.
3. The node (if present) will be removed from the tree visualization.

### Clearing the Tree: 
1. Click the CLEAR ALL button.
2. All nodes and edges will be removed from the tree.

----------------------------------------------------------

##Technical Notes

Dynamic Visualization:
- The spacing between nodes adjusts dynamically based on the depth of the tree, ensuring clarity in the visualization.
- The scrollbars allow navigation for larger trees.

Data Integrity:
- The application ensures the binary tree remains valid (e.g., no duplicate nodes, proper binary search tree structure).

Average depth:
- Average depth is calculated by summing depths for all nodes and then divide it by the total number of nodes.
