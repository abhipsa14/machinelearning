import os
from pathlib import Path
project_name = "projectstruct"

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/dataingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
]

for path in list_of_files:
    file_path = Path(path)
    filedir, filename=os.path.split(path)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
    if(not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass



