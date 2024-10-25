import unittest
from models.node import Node, OPERATOR
from services.ast_combiner import combine_rules
from services.rule_parser import create_rule

class TestASTCombiner(unittest.TestCase):

    def setUp(self):
        """Set up test rules."""
        self.rule1 = "((age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')) AND (salary > 50000 OR experience > 5)"
        self.rule2 = "((age > 30 AND department == 'Marketing')) AND (salary > 20000 OR experience > 5)"

    def test_combine_multiple_rules(self):
        """Test combining multiple rules into a single AST."""
        rules = [self.rule1, self.rule2]
        combined_ast = combine_rules(rules)
        
        # Check if the combined AST root is an OR operator (since the combiner uses OR to merge rules)
        self.assertIsInstance(combined_ast, Node)
        self.assertEqual(combined_ast.value, "OR")

    def test_combine_single_rule(self):
        """Test combining a single rule returns the correct AST."""
        rules = [self.rule1]
        combined_ast = combine_rules(rules)
        
        # Since it's a single rule, it should retain the top-level AND operator from rule1
        self.assertIsInstance(combined_ast, Node)
        self.assertEqual(combined_ast.value, "AND")

if __name__ == "__main__":
    unittest.main()
