from app import config
import os


def validate_data_graph():
    shacl_validation_command = f"shacl -d {config.config['data_graph']} -s {config.config['shape_graph']}"
    os.system(shacl_validation_command)
