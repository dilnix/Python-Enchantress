import re

text = 'some text around text'

# re.search()
# re.match()
# re.findall()
# re.finditer()
# re.sub()
# re.split()

patterns = {
    'mac': r'^([0-9a-f]{2}:){4}([0-9a-f]{2})',
    'home': r'localhost',
    'ip': r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$'
}


def foo(inp_string: str) -> None:
    for name, pattern in patterns.items():
        if re.match(pattern, inp_string):
            print(name)
            return
    print("Pattern doesn't match")


foo('192.168.1.1999')
foo('localhost')


def bar() -> dict:
    results = {}
    with open('data/django_success.log') as log_file:
        pattern = r'(?P<status_code>[\d]{3}) (?P<bytes>[\d]+)$'
        res = re.finditer(pattern, log_file.read(), flags=re.M)
        for match in res:
            status_code = match.group('status_code')
            results.setdefault(status_code, 0)
            results[status_code] += 1
    return results

key = '404'
res = {}

if key in res:
    print(res['key'])
else:
    res[key] = 0
    print(res[key])

res.get(key, 42)

s = "some password value"

print(re.sub(r'password', '******', s))
re.sub(r'\"POST /admin', '\"POST /secret_path', s)
'api_web          | [21/Apr/2020 10:19:44] "POST /admin/auto/carmodel/add/ HTTP/1.1" 302 0'
'api_web          | [21/Apr/2020 10:19:44] "POST /admin/auto/admin/carmodel/add/ HTTP/1.1" 302 0'
'api_web          | [21/Apr/2020 10:19:44] "POST /secret_path/auto/carmodel/add/ HTTP/1.1" 302 0'


print(bar())
