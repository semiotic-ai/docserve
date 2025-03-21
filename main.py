# system packages 
import json

# external packages
# ...

# internal packages
# ...

###########################################################################
# Goal                                                                    #
###########################################################################
# Your objective is to implement an API server that can generate documentation for a GraphQL schema. 
# You may use any external packages you want, but you do not have to. The goal is to see how you think about the problem. 


###########################################################################
# Base Classes (You may use these or implement your own)                  #
###########################################################################
class BaseModel:
    def __init__(self, config=dict()):
        self.config = config
        # self.config_value_one = config.get("config_value_one", "default")
        # ...
    
    def generate(self, prompt):
        return f"running inference for prompt: {prompt}"

###########################################################################
# Schema Parsing and Validation (You may use these or implement your own) #
###########################################################################
def parse_schema_ast(schema_str): 
    return schema_str

def validate_user_schema(gold, pred): 
    gold_ast = parse_schema_ast(gold)
    pred_ast = parse_schema_ast(pred)

    return gold_ast == pred_ast

###########################################################################
# API Server implementation (You may use these or implement your own)     #
###########################################################################

class DocumentationServer:
    """API Server for automating GraphQL schema documentation"""
    
    def __init__(self, config):
        self.base_model = BaseModel(config=config.get("model_config", {"...": "..."}))
    
    def add_model(self, model):
        """Add a new model to the server"""
        pass
    
    def document_schema(self, schema_str):
        """Document a GraphQL schema"""
        pass
    
    def start(self, port=8000):
        """Start the API server on the specified port"""
        # This is just a mock implementation
        print(f"Server started on port {port}")

###########################################################################
# This is just a mock implementation                                      # 
###########################################################################
def example():
    with open("example.graphql", "r") as f:
        schema = f.read()

    with open("config.json", "r") as f:     
        config = json.load(f)
    
    # create server
    server = DocumentationServer(config=config)

    # document schema
    docs = server.document_schema(schema)
    print(docs)
    
    # start server
    server.start()


if __name__ == "__main__":
    # Just a simple example to get started
    example()