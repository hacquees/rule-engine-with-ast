import os
from dotenv import load_dotenv
from services.rule_parser import create_rule as parse_rule
from services.ast_combiner import combine_rules as combine_ast_rules
from services.rule_evaluator import evaluate_rule as eval_rule
from models.database import Database

load_dotenv()

uri = os.getenv("MONGODB_URI")
if uri is None:
    raise ValueError("No MongoDB URI found in environment variables.")
db_name = "rule_engine"  
db = Database(uri, db_name)

def create_rule(rule_string):
    """Creates a rule and returns its AST representation."""
    ast = parse_rule(rule_string)
    inserted_id = db.insert_rule(repr(ast))  
    return ast, inserted_id  

def combine_rules(rules):
    """Combines a list of rules into a single AST."""
    combined_ast = combine_ast_rules(rules)
    inserted_id = db.insert_combined_rule(repr(combined_ast))  
    return combined_ast, inserted_id  

def evaluate_rule(ast, user_data):
    """Evaluates the given AST against user data."""
    return eval_rule(ast, user_data)
