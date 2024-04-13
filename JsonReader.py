import json
import re
from jsonschema import validate
class AWS_JSON_Reader:
    def __init__(self, JSON_schema_file_path:str)->None:
        self.JSON_schema_path = JSON_schema_file_path

    def verify_JSON(self, path_to_AWS_file: str)->None:
        with open(path_to_AWS_file,'rb') as f:
            try:
                jsonDict = json.load(f)
            except json.decoder.JSONDecodeError:
                print("EXCEPTION: Input file is not in JSON format.")
                raise
        with open(self.JSON_schema_path, 'rb') as f:
            jsonSchema = json.load(f)

        try:
            validate(jsonDict, jsonSchema) # jsonschema library function
            print("JSON data is valid.")
        except Exception as e:
            print(f"JSON data is invalid: {e.message}")
            raise


    def checkIfWildCardExists(self, path_to_AWS_file: str):
        with open(path_to_AWS_file, 'rb') as f:
            try:
                policy_json_dict = json.load(f)
            except json.decoder.JSONDecodeError:
                print("EXCEPTION: Input file is not in JSON format.")
                raise

        statement = policy_json_dict['PolicyDocument']['Statement']

        match statement:
            case dict():
                return statement['Resource'] == '*'
            case list():
                return any(s['Resource'] == '*' for s in statement)
        return False

    def verify_and_check_WildCard(self, path_to_AWS_file):
        self.verify_JSON(path_to_AWS_file)
        self.checkIfWildCardExists(path_to_AWS_file)


if __name__ == '__main__':
    reader = AWS_JSON_Reader('./AWS_IAM_Role_Policy_Schema.json')
    # reader.verify_JSON("./test_data/test_1.json")
    # if reader.checkIfWildCardExists("./test_data/test_1.json"):
    #     print("Resource in statement element equal *")
    reader.verify_and_check_WildCard("./test_data/test_1.json")
