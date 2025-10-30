
import tkinter as tk
from tkinter import *
import binary_tree as bt

#Creating font variable. This will be our main font for application
font = ('Times New Roman', 14, 'bold')

#class with methods we'll use to draw our tree
class Tree:
    def __init__(self, tree, canvas):
        self.tree = tree
        self.canvas = canvas
        #Creating integer variables, that we will be using in our to track number of nodes and depth of a tree
        self.nodesCount = tk.IntVar(value=0)
        self.averageDepth = tk.IntVar(value=None)
    
    """
    Now we're defining a method that recursively redraws our tree, starting from the
    root. It takes 4 variables: which node we need to draw, x, y coordinates where to draw node and 
    by using dx, we're making our tree actually look like a tree and it's not going too far from our window.
    """
    def draw_tree(self, node, x, y, dx, level, max_depth):
        if node is not None:
            radius = 20
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="lightblue", outline="black")
            self.canvas.create_text(x, y, text=str(node.value), font=font)

            # Calculate new horizontal spacing dynamically
            new_dx = max(dx * (1 - level / max_depth), 50)  # Minimum spacing of 50

            if node.left is not None:
                x_end = x - new_dx
                y_end = y + 80
                self.canvas.create_line(x, y + radius, x_end, y_end - radius, arrow=tk.LAST)
                self.draw_tree(node.left, x_end, y_end, new_dx, level + 1, max_depth)

            if node.right is not None:
                x_end = x + new_dx
                y_end = y + 80
                self.canvas.create_line(x, y + radius, x_end, y_end - radius, arrow=tk.LAST)
                self.draw_tree(node.right, x_end, y_end, new_dx, level + 1, max_depth)
                
    #function, that completely redraws the tree
    def update_canvas(self):
        self.canvas.delete("all")
        self.nodesCount.set(self.tree.size())
        self.averageDepth.set(self.tree.avg_tree_depth())
        
        max_depth = self.tree.depth()
        width = min(1024 + 200 * 2 ** (max_depth - 1), 3000)
        height = max(720, 100 + 80 * max_depth) 
        self.canvas.config(scrollregion=(0, 0, width, height))
        self.draw_tree(self.tree.root, width//3, 40, 300, 1, max_depth)
        
    #Here we are creating a frame for "add" label, button, command and entry field
    def addNode(self, entry):
        val = int(entry.get())
        val = int(val)
        self.tree.add(val)
        self.update_canvas()

        
    #Here we are creating a frame for "remove" label, button, command and entry field
    def removeNode(self, entry):
        val = int(entry.get())
        val = int(val)
        self.tree.remove(val)
        self.update_canvas()
        
    def clearAll(self):
        self.tree.clear()
        self.update_canvas()

#class with all UI/tkinter methods
class VisualizerApp:
    def __init__(self):
        #Creating root, setting window title and size
        self.root = tk.Tk() 
        self.root.title('Binary tree')
        self.root.state('zoomed')

        #creating binary tree data structure, which will contain our nodes
        self.binTree = bt.TreeSet()
        
        #calling method which setups our ui
        self.setupUi()
        
    def setupUi(self):
        """
        Application window is divided in 2 major parts: big left frame with all 
        functionality('add', 'remove', 'clear all' buttons) and big right canvas
        where our nodes should be displayed.

        Big left frame should be divided into smaller frames
        """
        #Creating left frame
        leftFrame = tk.Frame(self.root, bg='gray53', width = 250, height = 720)
        leftFrame.pack_propagate(False) 
        leftFrame.pack(side="left", fill= 'y')

        #creating canvas and frame for it, where our tree will be displayed
        canvasFrame = tk.Frame(self.root)
        canvasFrame.pack(fill='both', expand=True)
        canvas = tk.Canvas(canvasFrame, scrollregion= (0, 0, 1000, 1000))

        #adding x and y scrollbars for more convenient view
        yScroll = tk.Scrollbar(canvasFrame, orient= 'vertical', command= canvas.yview)
        yScroll.pack(side= 'right', fill = 'y')
        xScroll = tk.Scrollbar(canvasFrame, orient= 'horizontal', command= canvas.xview)
        xScroll.pack(side='bottom', fill='x')

        #packing canvas after scrolls, othw it looks bad
        canvas.pack(fill='both', expand= True)

        canvas.config(xscrollcommand= xScroll.set, yscrollcommand= yScroll.set)

        tree = Tree(self.binTree, canvas)

        """ 
        Now we are creating frame for upper labels. It should contain
        'Number of nodes' and 'Average depth' labels. Also this is
        where we use our integer variable we created before
        """
        upLabelsFrame = tk.Frame(leftFrame, bg='gray53')
        upLabelsFrame.pack(anchor='w', fill='x')
        tk.Label(upLabelsFrame, text="Number of nodes:", bg="gray53", font=font).grid(pady=10, padx=10,row=0, column=0)
        tk.Label(upLabelsFrame, textvariable=tree.nodesCount, bg='gray53', font= font, width=10).grid(row=0, column=1)
        tk.Label(upLabelsFrame, text="Average depth:", bg="gray53", font=font).grid(pady=10, padx=10, row = 1, column = 0)
        tk.Label(upLabelsFrame, textvariable= tree.averageDepth, bg='gray53', font= font).grid(row=1, column=1)

        addFrame = tk.Frame(leftFrame, bg= 'gray53')
        addFrame.pack(anchor="w", fill='x')
        tk.Label(addFrame, text='Enter value of a node\n you want to add:', bg='gray53', font= font).grid(row= 0, column= 0, padx=0)
        entryAdd = tk.Entry(addFrame, bg="lightgray", width=20)
        entryAdd.grid(row=1, column= 0)
        tk.Button(addFrame, text="ADD", bg="lightgray", font=font, command= lambda: tree.addNode(entryAdd)).grid(row=0,rowspan=2, column=1, pady= 20)

        removeFrame = tk.Frame(leftFrame, bg = 'gray53', pady = 30)
        removeFrame.pack(anchor = "w", fill = 'x')
        tk.Label(removeFrame, text = 'Enter value of a node\n you want to remove:', bg ='gray53', font = font).grid(row = 0, column= 0, padx=0)
        entryRemove = tk.Entry(removeFrame, bg = "lightgray", width = 20)
        entryRemove.grid(row = 1, column = 0)
        tk.Button(removeFrame, text="DEL", bg="lightgray", font = font, command = lambda: tree.removeNode(entryRemove)).grid(row = 0,rowspan = 2, column = 1, pady= 20)

        #Here we are creating CLEAR ALL button and command for it, which should clear our binary tree
        tk.Button(leftFrame, text = 'CLEAR ALL', bg = 'lightgray', font = font, command = lambda: tree.clearAll()).pack()
        
    def run(self):
        self.root.mainloop()        

App = VisualizerApp()
App.run()
