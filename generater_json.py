
import json
from collections import OrderedDict

file_data = OrderedDict()

# print()
print("'test'" + str(1))

str1 = ""

for i in range(1, 120):
    file_data["name"] = str(i)
    file_data["alias"] = str(i)
    file_data["type"] = "DOUBLE"
    file_data["logicalType"] = "DOUBLE"
    file_data["role"] = "MEASURE"
    file_data["seq"] = i
    str1 += json.dumps(file_data, ensure_ascii=False, indent="\t") + ","


print(str1)