# coding:utf8
import jsonpath,json


s = '{"status": 405, "msg": "非法请求"}'

jsonres = json.loads(s)
r = jsonpath.jsonpath(jsonres, "status")
print(str(r[0])=="405")

print(jsonres['status'])
