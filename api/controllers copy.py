from services.rule_parser import create_rule as parse_rule
from services.ast_combiner import combine_rules as combine_ast_rules
from services.rule_evaluator import evaluate_rule as eval_rule
from models.database import Database

# Initialize database connection
uri = "mongodb+srv://hacquees:qwerty101@cluster0.c5u9o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  
db_name = "rule_engine"  
db = Database(uri, db_name)

def create_rule(rule_string):
    """Creates a rule and returns its AST representation."""
    ast = parse_rule(rule_string)
    inserted_id = db.insert_rule(repr(ast))  # Store the string representation of the AST
    return ast, inserted_id  # Return both AST and its ID

def combine_rules(rules):
    """Combines a list of rules into a single AST."""
    combined_ast = combine_ast_rules(rules)
    inserted_id = db.insert_combined_rule(repr(combined_ast))  # Store the combined AST representation
    return combined_ast, inserted_id  # Return both combined AST and its ID

def evaluate_rule(ast, user_data):
    """Evaluates the given AST against user data."""
    return eval_rule(ast, user_data)
