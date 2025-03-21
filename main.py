# system packages 
import sys
import json
import logging

# external packages
# ...

# internal packages
# ...

# logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

###########################################################################
# Goal                                                                    #
###########################################################################

# Your objective is to implement an API server that can generate documentation for a GraphQL schema. 
# You may use any external packages you want, but you do not have to. The goal is to see how you think about the problem. 
# You are free to implement any additional helper functions you want. 

# Additional resources include:
# - config.json (server configuration and initial model list)
# - new_model_config.json (new model configuration)
# - example.graphql (example GraphQL schema)

###########################################################################
# Helper Functions (You may add any additional functions as you see fit)  #
###########################################################################

def parse_schema_ast(schema_str): 
    return schema_str

def validate_user_schema(gold, pred): 
    gold_ast = parse_schema_ast(gold)
    pred_ast = parse_schema_ast(pred)

    return gold_ast == pred_ast


###########################################################################
# Base Classes (Please implement. You may add more classes as needed)     #
###########################################################################

class BaseModel:
    def __init__(self, config):
        # please implement
        pass
    
    def generate(self, prompt):
        # mock implementation
        return prompt


###########################################################################
# API Server implementation (Please implement as you see fit)             #
###########################################################################

class DocumentationServer:
    """API Server for automating GraphQL schema documentation"""
    
    def __init__(self, config):
        # please implement
        pass
    
    def add_model(self, model):
        """Add a new model to the server"""
        # please implement
        pass

    def get_models(self):
        """Get all models from the server"""
        # please implement
        pass

    def document_schema(self, schema_str):
        """Document a GraphQL schema"""
        # please implement the logic for documenting the schema. 
        # NOTE: for sake of simplicity, to pass the tests, simply return the input schema_str as the output
        # we just care about your logic here. 
        pass
    
    def start(self, port=8000):
        """Start the API server on the specified port"""
        # this is just a mock implementation. feel free to change it as you see fit.
        logger.info(f"Server started on port {port}")

    # add any additional functions as you see fit


################################################################
# Tests (Please do not modify existing tests unless specified) #
################################################################

# python main.py test
def test():
    logger.info("hello, world!")

# helper function to create a documentation server
def documentation_server():
    with open("config.json", "r") as f:     
        config = json.load(f)
    
    server = DocumentationServer(config=config)
    return server

def test_documentation_server():
    server = documentation_server()
    assert server is not None
    assert isinstance(server, DocumentationServer)

def test_get_models():
    server = documentation_server()
    assert server.get_models() == ["model_one", "model_two"]

def test_add_model():
    with open("new_model_config.json", "r") as f:     
        model_config = json.load(f)
    
    server = documentation_server()
    server.add_model(model_config)
    assert server.get_models() == ["model_one", "model_two", "model_three"]

def test_document_schema():
    with open("example.graphql", "r") as f:
        schema = f.read()
    
    server = documentation_server()
    documented_schema = server.document_schema(schema)
    assert documented_schema == schema

def test_start():
    # feel free to change this as you see fit
    server = documentation_server()
    server.start()

# please feel free to add any additional tests! 

def test_all():
    try:
        test_documentation_server()
        logger.info("test_documentation_server: passed")
    except: 
        logger.error("test_documentation_server: failed")

    try:
        test_get_models()
        logger.info("test_get_models:           passed")
    except:
        logger.error("test_get_models:           failed")

    try:
        test_add_model()
        logger.info("test_add_model:            passed")
    except:
        logger.error("test_add_model:            failed")

    try:
        test_document_schema()
        logger.info("test_document_schema:      passed")
    except:
        logger.error("test_document_schema:      failed")

    try:
        test_start()
        logger.info("test_start:                passed")
    except:
        logger.error("test_start:                failed")

##########################################
# Main
##########################################

if __name__ == "__main__":
    globals()[sys.argv[1]]()