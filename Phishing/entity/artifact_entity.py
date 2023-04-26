from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    train_file_path:str
    test_file_path:str
    base_data_path:str