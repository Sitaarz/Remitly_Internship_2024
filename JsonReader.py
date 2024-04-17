import json
from jsonschema import validate


class AWS_JSON_Reader:
    def __init__(self, JSON_schema_file_path: str) -> None:
        self.JSON_schema_path = JSON_schema_file_path

    def verify_JSON(self, path_to_AWS_file: str) -> None:
        with open(path_to_AWS_file, 'rb') as f:
            try:
                jsonDict = json.load(f)
            except json.decoder.JSONDecodeError:
                print("EXCEPTION: Input file is not in JSON format.")
                raise
        with open(self.JSON_schema_path, 'rb') as f:
            jsonSchema = json.load(f)

        try:
            validate(jsonDict, jsonSchema)  # jsonschema library function
            print("JSON data is valid.")
        except Exception as e:
            print(f"JSON data is invalid: {e.message}")
            raise

    def checkIfWildCardExists(self, path_to_AWS_file: str) -> bool:
        with open(path_to_AWS_file, 'rb') as f:
            try:
                policy_json_dict = json.load(f)
            except json.decoder.JSONDecodeError:
                print("EXCEPTION: Input file is not in JSON format.")
                raise

        statement = policy_json_dict['PolicyDocument']['Statement']

        match statement:
            case dict():
                return statement.get('Resource', '') != '*'
            case list():

                return all(s.get('Resource', '') != '*' for s in statement)
        return False

    def verify_and_check_WildCard(self, path_to_AWS_file: str) -> bool:
        self.verify_JSON(path_to_AWS_file)
        return self.checkIfWildCardExists(path_to_AWS_file)


if __name__ == '__main__':
    reader = AWS_JSON_Reader('./AWS_IAM_Role_Policy_Schema.json')
    print(reader.verify_and_check_WildCard(
        "./test_false_data/test_one_list_element.json"))
