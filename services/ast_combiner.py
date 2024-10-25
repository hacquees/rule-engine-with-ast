from models.node import Node, OPERATOR, OPERAND
from services.rule_parser import create_rule

def combine_rules(rules):
    if not rules:
        return None

    combined_ast = create_rule(rules[0])
    for rule in rules[1:]:
        new_rule = create_rule(rule)
        combined_ast = Node(OPERATOR, "OR", left=combined_ast, right=new_rule)
    return combined_ast
    