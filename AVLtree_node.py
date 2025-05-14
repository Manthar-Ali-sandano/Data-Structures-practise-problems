class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = self.right = None
