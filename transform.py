from rdflib import Graph
from app import config

def merge_all_dataset(paths: list):
    merged_dataset = str()
    for each_dataset in paths:
        with open(each_dataset,"r") as reader:
            merged_dataset = merged_dataset + reader.read()
    return merged_dataset


def create_graph(merged_dataset):
    source_graph = Graph()
    source_graph.parse(data=merged_dataset, format="nt")
    return source_graph


def execute_mapping(source_graph, mapping):
    return source_graph.query(mapping).serialize(format="turtle")


def save(graph):
    with open(config.config["data_graph"], "wb") as graph_writer:
        graph_writer.write(graph)
