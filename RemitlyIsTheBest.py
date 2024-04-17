import sys
from JsonReader import AWS_JSON_Reader

aws_reader = AWS_JSON_Reader('AWS_IAM_Role_Policy_Schema.json')
argument = sys.argv[1:]

if len(argument) != 1:
    print("Number of arguments not correct. Only absolute path to JSON file is expected.")
    sys.exit()

result = aws_reader.verify_and_check_WildCard(argument[0])
print("Method returns:", result)

sys.exit()
