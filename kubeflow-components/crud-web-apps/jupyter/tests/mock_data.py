import json
import pathlib
import os
#from .. import utils

# from kubeflow.kubeflow.crud_backend import helpers

# NAMESPACE = "kubeflow-user"

# def get_mock_body():
#     with open("/src/apps/common/tests/mock_body.json", "r") as body_file:
#         return json.loads(body_file.read())

# def get_mock_notebook():
#     mock_notebook = helpers.load_param_yaml(
#         utils.NOTEBOOK_TEMPLATE_YAML,
#         name=get_mock_body()["name"],
#         namespace=NAMESPACE,
#         serviceAccount="default-editor",
#     )
#     return mock_notebook

path = pathlib.Path().resolve().as_posix()+"/tests"
# path = os.environ['VIRTUAL_ENV']

def get_mock_data(data):
    with open(path + data, "r") as f:
        return json.loads(f.read())
