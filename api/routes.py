import json
import traceback 
from flask import request, jsonify
from models.node import Node
from .controllers import create_rule, combine_rules, evaluate_rule
from . import api_blueprint

@api_blueprint.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    """Endpoint to create a new rule."""
    data = request.json
    if not data or "rule_string" not in data:
        return jsonify({"error": "Missing 'rule_string' in request data"}), 400

    rule_string = data["rule_string"]
    
    try:
        ast, inserted_id = create_rule(rule_string)  # Unpack the tuple returned by create_rule
        return jsonify({"ast": repr(ast), "inserted_id": str(inserted_id)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_blueprint.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    """Endpoint to combine multiple rules into one AST and store in the database."""
    data = request.json
    if not data or "rules" not in data:
        return jsonify({"error": "Missing 'rules' in request data"}), 400

    rules = data["rules"]
    try:
        combined_ast, combined_rule_id = combine_rules(rules)  # Unpack the tuple returned by combine_rules
        return jsonify({"combined_ast": repr(combined_ast), "combined_rule_id": str(combined_rule_id)}), 200 
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@api_blueprint.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json
    print("Received data:", data)  # Debug print
    ast_data = data.get("ast")
    user_data = data.get("user_data")

    if not ast_data or not user_data:
        return jsonify({"error": "Missing 'ast' or 'user_data' in request data"}), 400

    try:
        result = evaluate_rule(ast_data, user_data)  # Call your evaluate function
        return jsonify({"result": result}), 200
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format for 'ast'"}), 400
    except Exception:
        print(traceback.format_exc())
        return jsonify({"error": str("AAa")}), 500