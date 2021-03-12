import re

'''
Running this file with Python3 Interpreter will get contains of input
file called config.ini, replace all values where configuration keys
contains words like "id", "key", "secret" and "password" with
expression "XXXXXX", and then write updated content to output
file called config_updated.ini.
'''

pattern = r'(id|key|secret|password)( = |": ")(?P<value>.[^"^\n]+)'

with open('./config.ini', 'r') as input, open('./config_updated.ini', 'w') as output:
    content = input.read()
    updated = re.sub(pattern, r'\g<1>\g<2>XXXXXX', content, flags=re.M)
    output.write(updated)
