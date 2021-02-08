from app import transform, validator, config
if __name__ == "__main__":
    transform.save(
        transform.execute_mapping(
            transform.create_graph(
                transform.merge_all_dataset(config.config["datasets"])), open(config.config["mapping"], "r").read()))
    print("Initial Knowledge Graph Created!")
    validator.validate_data_graph()
    print("Initial Knowledge Graph Validated!")
