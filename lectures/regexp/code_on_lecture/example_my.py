import re

with open("./django_success.log", "r") as f:
    data = f.read()
    pattern = r'(?P<status_code>[\d]{3}) (?P<bytes>[\d]+)$'
    found = re.finditer(pattern, data, flags=re.MULTILINE)
    print(sum(
        (int(match.group('bytes')) for match in found)
    ))


def statuses() -> dict:
    results = {}
    with open("./django_success.log", "r") as f:
        data = f.read()
        pattern = r'(?P<status_code>[\d]{3}) (?P<bytes>[\d]+)$'
        found = re.finditer(pattern, data, flags=re.MULTILINE)
        for match in found:
            status_code = match.group('status_code')
            results.setdefault(status_code, 0)
            results[status_code] += 1
    return results


print(statuses())


text = '''
api_web          | [21/Apr/2020 10:19:17] "GET /favicon.ico HTTP/1.1" 404 2486
api_web          | [21/Apr/2020 10:19:25] "POST /admin/auto/carbrand/ HTTP/1.1" 200 5559
api_web          | [21/Apr/2020 10:19:25] "GET /static/admin/js/cancel.js HTTP/1.1" 200 409
api_web          | [21/Apr/2020 10:19:27] "POST /admin/auto/carbrand/ HTTP/1.1" 302 0
api_web          | [21/Apr/2020 10:19:27] "GET /admin/auto/carbrand/ HTTP/1.1" 200 19114
api_web          | [21/Apr/2020 10:19:28] "GET /admin/jsi18n/ HTTP/1.1" 200 3223
api_web          | [21/Apr/2020 10:19:29] "GET /admin/auto/ HTTP/1.1" 200 5588
'''

print(re.sub(r'POST \/admin', 'POST /secret_path', text))
