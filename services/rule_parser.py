from models.node import Node, OPERATOR, OPERAND

import re

def make_tokens(expression):
    expression = expression.upper()
    tokens = re.findall(r'\w+|!=|<=|>=|==|<|>|AND|OR|\(|\)', expression)
    return tokens

precedence = {
    "(": 0,   
    ")": 0,   
    "AND": 1,
    "OR": 1,
    "<=": 2,
    ">=": 2,
    "==": 2,
    "!=": 2,
    "<": 2,
    ">": 2,
    "+": 3,
    "-": 3,
    "*": 4
}

def infix_to_postfix(tokens):
    """
    Converts an infix expression represented by tokens to postfix notation.

    Args:
        tokens: A list of tokens representing the infix expression.

    Returns:
        A list of tokens representing the postfix expression.
    """

    stack = []
    postfix = []

    for token in tokens:
        if token not in precedence and token not in "()":
            postfix.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[stack[-1]] >= precedence[token]:
                postfix.append(stack.pop())
            stack.append(token)

    while stack:
        postfix.append(stack.pop())

    return postfix




def postfix_to_ast(postfix):
  """
  Converts a postfix expression represented by tokens to an AST.

  Args:
      postfix: A list of tokens representing the postfix expression.

  Returns:
      The root node of the AST.
  """
  stack = []

  for token in postfix:
    if token in precedence:  # Operator
      right = stack.pop()
      left = stack.pop()
      node = Node(OPERATOR, token, left, right)
      stack.append(node)
    else:  # Operand
      node = Node(OPERAND, token)
      stack.append(node)

  if len(stack) != 1:
    raise ValueError("Invalid postfix expression")

  return stack[0]


def create_rule(rule_string):
    tokens = make_tokens(rule_string)     #, ["(", ")","AND", "OR","<=", ">=", "==","!=" ,"<", ">", "+", "-", "*" ])
    print(tokens)
    # Output: ['A', '>', '3', 'AND', 'A', '<', '4', 'OR', '(', 'FD', '>', '4', 'AND', 'ASD', '<', '3', ')']
    # Now just covert this to post-fix

    postfix = infix_to_postfix(tokens)
    print("dd",postfix)
    return postfix_to_ast(postfix)



# rule_string = "Name == Ankit or (age < 18 and marks >= 80) or (age > 18 and marks >= 60) or (age == 18 and marks != 60 and (name == Priya or name == Prachi))"
# print("sxreate",create_rule(rule_string))
