import os
from pymongo import MongoClient
from dotenv import load_dotenv

class Database:
    def __init__(self, uri=None, db_name="rule_engine"):
        load_dotenv() 
        self.uri = uri or os.getenv("MONGODB_URI") 
        if self.uri is None:
            raise ValueError("A valid MongoDB URI must be provided.")
        
        self.client = MongoClient(self.uri)
        
        try:
            self.client.admin.command('ping')
            print("MongoDB connected successfully.")
        except Exception as e:
            print(f"Failed to connect to MongoDB: {e}")
        
        self.db = self.client[db_name]
        self.rules_collection = self.db["rules"]

    def insert_rule(self, ast):
        """Inserts a new rule AST into the database and returns its ID."""
        rule_data = {"rule_string": ast}
        return self.rules_collection.insert_one(rule_data).inserted_id

    def insert_combined_rule(self, combined_rule):
        """Inserts a combined rule into the database and returns its ID."""
        rule_data = {"combined_rule": combined_rule}
        return self.rules_collection.insert_one(rule_data).inserted_id
