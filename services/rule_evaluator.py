import json
from models.node import OPERATOR, OPERAND, Node

def parse_string(s):
    """Parses a string to the appropriate data type."""
    
    if s.lower() in ['true', 'false']:
        return s.lower() == 'true'

    try:
        return int(s)
    except ValueError:
        pass

    try:
        return float(s)
    except ValueError:
        pass

    return s

def parse_node(node_dict):
    """Parses a node."""
    if node_dict["type"] == OPERAND:
        return Node(OPERAND, node_dict["value"])
    elif node_dict["type"] == OPERATOR:
        left_node = parse_node(node_dict["left"])
        right_node = parse_node(node_dict["right"])
        return Node(OPERATOR, node_dict["value"], left=left_node, right=right_node)

def evaluate_rule(ast, user_data):
    """Evaluates the given AST against user data."""
    print("userdata", user_data)
    operator_funcs = {
        "AND": lambda left, right: left and right,
        "OR": lambda left, right: left or right,
        ">": lambda left, right: parse_string(left) > parse_string(right),
        "<": lambda left, right: parse_string(left) < parse_string(right),
        ">=": lambda left, right: parse_string(left) >= parse_string(right),
        "<=": lambda left, right: parse_string(left) <= parse_string(right),
        "==": lambda left, right: left == right,
        "!=": lambda left, right: left != right,
        "+": lambda left, right: parse_string(left) + parse_string(right),
        "-": lambda left, right: parse_string(left) - parse_string(right),
        "*": lambda left, right: parse_string(left) * parse_string(right),
    }

    def eval_node(node):
        """Recursively evaluates the AST node."""
        node_type = node.type
        
        if node_type == OPERAND:
            return user_data.get(node.value, node.value)

        if node_type == OPERATOR:
            operator_value = node.value
            left_val = eval_node(node.left)
            right_val = eval_node(node.right)
            
            if operator_value in operator_funcs:
                print(left_val, operator_value, right_val, operator_funcs[operator_value](left_val, right_val))
                return operator_funcs[operator_value](left_val, right_val)
        
        raise ValueError(f"Unknown node type: {node_type}")

    if type(ast) != Node:
        ast_dict = json.loads(ast)
        ast = parse_node(ast_dict)
        return eval_node(ast)
    else:
        return eval_node(ast)
