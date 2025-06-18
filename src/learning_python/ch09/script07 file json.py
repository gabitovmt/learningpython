# JSON

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec)
# {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}

import json
S = json.dumps(rec)
print(S)
# {"name": {"first": "Bob", "last": "Smith"}, "job": ["dev", "mgr"], "age": 40.5}

O = json.loads(S)
print(O)
# {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}

print(O == rec)
# True

json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())
# {
#     "name": {
#         "first": "Bob",
#         "last": "Smith"
#     },
#     "job": [
#         "dev",
#         "mgr"
#     ],
#     "age": 40.5
# }