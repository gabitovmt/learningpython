import os
from pathlib import Path

testLog = os.path.abspath('test.log')
testLogOld = os.path.normpath(os.path.join(testLog, os.pardir, 'test.log.old'))

print(testLog)
print(testLogOld)

testLogP = Path().resolve().joinpath('test.log')
testLogOldP = Path(testLogP, os.pardir, 'test.log.old').resolve()

print(testLogP)
print(testLogOldP)

parDir = Path(os.pardir).resolve()
print(parDir)
