# system packages 
import os
import logging
from pathlib import Path
# internal packages

# external packages
import graphdoc
from dotenv import load_dotenv

# configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# load the environment variables
load_dotenv("../.env")

# global variables
assets_dir = Path(__file__).resolve().parent.parent.parent / "assets"
yaml_path = assets_dir / "config.yaml"
schema_path = assets_dir / "schema.graphql"


def main():
    log.info("Starting DocServe...")

    # load the generator
    generator = graphdoc.doc_generator_module_from_yaml(yaml_path)

    # load the mlflow data helper
    mdh = graphdoc.mlflow_data_helper_from_yaml(yaml_path)
    mdh.set_auth_env_vars()

    # load the schema
    with open(schema_path, "r") as f:
        schema = f.read()

    # generate the documentation
    documented_schema = generator.document_full_schema(
       database_schema=schema,
       trace=True,
       client=mdh.mlflow_client,
       expirement_name="interview",
       logging_id="interview",
    )

    # save the documentation
    with open(assets_dir / "documented_schema.graphql", "w") as f:
        f.write(documented_schema.documented_schema)

if __name__ == "__main__":
    main()

