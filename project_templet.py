import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format="[%(asctime)s]:%(message)s")
project_name = "Phishing"

list_of_files = [
        ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "docs/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation",
    f"{project_name}/components/data_transformation",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/components/model_validate.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/traning_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for f in list_of_files:
    file_path = Path(f)

    filedir,filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass
        logging.info(f"Creating empty file {filename}")

    else:
        logging.info(f"{filename} already exist")