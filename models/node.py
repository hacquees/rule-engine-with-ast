import json

OPERATOR = "operator"
OPERAND = "operand"

class Node:
    def __init__(self, type, value, left=None, right=None):
        self.type = type          # "operator" or "operand"
        self.left = left          # Reference to left child
        self.right = right        # Reference to right child (if operator)
        self.value = value

    def __repr__(self):
        return json.dumps(self.data())

    def data(self):
        if self.type==OPERAND:
            return {"type":OPERAND,
            "value":self.value}
        return {
            "type":OPERATOR,
            "value":self.value,
            "left":self.left.data(),
            "right":self.right.data()
            
        }