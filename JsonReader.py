import json
import re
from jsonschema import validate
class AWS_JSON_Reader:

    def check_policy_name(self, jsonDict: dict)->None:
        if 'PolicyName' not in jsonDict.keys():
            raise ValueError('No PolicyName attribute in JSON.')

        name_pattern = '[\\w+=,.@-]{1,128}'
        if not re.match(name_pattern, jsonDict['PolicyName']):
            raise ValueError('PolicyName does not match pattern.')

    def check_policyDocument(self, policyDict: dict):
        pass

    def verifie_json(self, file: str)->bool:
        with open(file,'rb') as f:
            try:
                jsonDict = json.load(f)
            except json.decoder.JSONDecodeError as e:
                print("EXCEPTION: Input file is not in JSON format.")
                raise

        self.check_policy_name(jsonDict)
        try:
            self.check_policyDocument(jsonDict['PolicyDocument'])
        except KeyError:
            print("No PolicyDocument attribute")
            raise


if __name__ == '__main__':
    reader = AWS_JSON_Reader()
    reader.verifie_json("./data/test_1.json")
