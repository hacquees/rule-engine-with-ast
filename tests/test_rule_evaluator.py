import unittest
from services.rule_evaluator import evaluate_rule
from services.rule_parser import create_rule

class TestRuleEvaluator(unittest.TestCase):

    def setUp(self):
        """Set up user data and create rules using create_rule."""
        self.user_data_1 = {
            "AGE": "32",
            "DEPARTMENT": "SALES",
            "SALARY": "55000",
            "EXPERIENCE": "6"
        }
        
        self.user_data_2 = {
            "AGE": "22",
            "DEPARTMENT": "MARKETING",
            "SALARY": "30000",
            "EXPERIENCE": "3"
        }

        self.user_data_3 = {
            "AGE": "31",
            "DEPARTMENT": "MARKETING",
            "SALARY": "18000",
            "EXPERIENCE": "6"
        }

        # Create rules using create_rule
        self.rule1 = create_rule("((AGE > 30 AND DEPARTMENT == 'Sales') OR (AGE < 25 AND DEPARTMENT == 'Marketing')) AND (SALARY > 50000 OR EXPERIENCE > 5)")
        self.rule2 = create_rule("((AGE > 30 AND DEPARTMENT == 'Marketing')) AND (SALARY > 20000 OR EXPERIENCE > 5)")

    def test_evaluate_rule1_true(self):
        """Test rule1 evaluation with user_data_1, expecting a match."""
        result = evaluate_rule(self.rule1, self.user_data_1)
        print(f"Rule 1 evaluation (True) result: {result}")  # Debugging line
        self.assertTrue(result)

    def test_evaluate_rule1_false(self):
        """Test rule1 evaluation with user_data_3, expecting no match."""
        result = evaluate_rule(self.rule1, self.user_data_3)
        print(f"Rule 1 evaluation (False) result: {result}")  # Debugging line
        self.assertFalse(result)

    def test_evaluate_rule2_true(self):
        """Test rule2 evaluation with user_data_3, expecting a match."""
        result = evaluate_rule(self.rule2, self.user_data_3)
        print(f"Rule 2 evaluation (True) result: {result}")  # Debugging line
        self.assertTrue(result)

    def test_evaluate_rule2_false(self):
        """Test rule2 evaluation with user_data_2, expecting no match."""
        result = evaluate_rule(self.rule2, self.user_data_2)
        print(f"Rule 2 evaluation (False) result: {result}")  # Debugging line
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
