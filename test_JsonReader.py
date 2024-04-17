import unittest
from JsonReader import AWS_JSON_Reader
from json.decoder import JSONDecodeError
from jsonschema.exceptions import ValidationError
import os


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.reader = AWS_JSON_Reader('AWS_IAM_Role_Policy_Schema.json')

    def test_JSON_wrong_syntax(self):
        self.assertRaises(
            JSONDecodeError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_wrong_JSON_syntax_1.json')
        self.assertRaises(
            JSONDecodeError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_wrong_JSON_syntax_2.json')

    def test_no_policyName(self):
        self.assertRaises(
            ValidationError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_no_policyName.json')

    def test_no_policyDocument(self):
        self.assertRaises(
            ValidationError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_no_policyDocument.json')

    def test_0_statements(self):
        self.assertRaises(
            ValidationError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_0_statements.json')

    def test_many_statements(self):
        try:
            self.reader.verify_and_check_WildCard(
                './test_wrong_syntax_data/test_many_statements.json')
        except ValidationError:
            self.fail("App does not allow for many statements.")

    def test_no_version(self):
        self.assertRaises(
            ValidationError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_no_version.json')

    # we are creating IAM permissions policy so we can not add principal
    def test_file_with_principal(self):
        self.assertRaises(
            ValidationError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_with_principal.json')

    def test_action(self):
        self.assertRaises(
            ValidationError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_no_action.json')
        self.assertRaises(
            ValidationError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_no_elements_action.json')

    def test_notAction(self):
        self.assertRaises(
            ValidationError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_no_action.json')
        self.assertRaises(
            ValidationError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_aciton_not_action.json')
        # Action and notAction can not be in the same object

    def test_resorce_notResorce(self):
        self.assertRaises(
            ValidationError,
            self.reader.verify_and_check_WildCard,
            './test_wrong_syntax_data/test_resorce_notResorce.json')
        # Resorce and notResorce can not be in the same object

    def test_true_value(self):
        file_list = os.listdir('test_true_data')
        for fileName in file_list:
            result = self.reader.verify_and_check_WildCard(
                f'./test_true_data/{fileName}')
            self.assertTrue(result, f'File {fileName} verification failed')

    def test_false_value(self):
        file_list = os.listdir('test_false_data')
        for fileName in file_list:
            result = self.reader.verify_and_check_WildCard(
                f'./test_false_data/{fileName}')
            self.assertFalse(result, f'File {fileName} verification failed')


if __name__ == '__main__':
    unittest.main()
