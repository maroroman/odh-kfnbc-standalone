import json

def get_mock_body():
    with open("mock_body.json", "r") as body_file:
        return json.loads(body_file.read())