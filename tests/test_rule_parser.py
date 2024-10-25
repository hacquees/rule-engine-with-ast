import unittest
from services.rule_parser import create_rule
from models.node import Node, OPERATOR, OPERAND

class TestRuleParser(unittest.TestCase):

    def test_create_rule_ast(self):
        """Test parsing rule string into AST."""
        rule_string = "age > 30 AND department == 'Sales'"
        ast = create_rule(rule_string)
        
        self.assertIsInstance(ast, Node)
        self.assertEqual(ast.value, "AND")
        self.assertEqual(ast.left.value, ">")
        self.assertEqual(ast.right.value, "==")

    def test_complex_rule(self):
        """Test parsing a more complex rule."""
        rule_string = "((age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')) AND (salary > 50000 OR experience > 5)"
        ast = create_rule(rule_string)
        
        self.assertIsInstance(ast, Node)
        self.assertEqual(ast.value, "AND")

if __name__ == "__main__":
    unittest.main()
