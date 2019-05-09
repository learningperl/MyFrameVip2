# coding:utf8
import requests, json


class HTTP():
    """
    http协议接口测试的关键字类
    提供调用http接口的各种方法
    提供接口测试结果断言的各种方法
    """

    def __init__(self):
        # 在创建对象的时候初始化session
        self.session = requests.session()
        # 设置请求的基本url
        self.url = ""
        self.params = {}
        self.result = None
        self.jsonres = None
        self.json = {}

    def seturl(self, u):
        # 设置请求的基本url
        self.url = u + "/"

    def removeheader(self, key):
        # 从请求的头里面删除key这个键
        try:
            self.session.headers.pop(key)
        except Exception as e:
            print(e)

    def addheader(self,key,value):
        # 往请求的头里面添加一个键值对
        value = self.__get_value(value)
        self.session.headers[key] = value

    def post(self, path, params=None):
        # 解析参数为一个dict
        self.__get_params(params)
        # 调用post，请求接口
        self.result = self.session.post(self.url + path, data=self.params)
        self.jsonres = json.loads(self.result.text)

    def __get_params(self, p):
        # 每一次解析参数之前先清空参数dict
        self.params.clear()

        if p is None:
            return self.params

        # 分割每一个参数
        pp = p.split('&')
        for s in pp:
            # 分割每一个参数的键和值
            ppp = s.split('=')
            self.params[ppp[0]] = ppp[1]

        return self.params

    def assertequals(self, key, value):
        """
        校验返回的json结果里面，key对应的值是否和预期的value一致
        :param key: 要校验的json的键
        :param value: 期望值
        :return: 无
        """
        if str(self.jsonres[key]) == value:
            print("PASS")
        else:
            print("FAIL")

    def savejson(self,key,p):
        """
        将返回结果里面，json的key的值，保存到我们框架的p这个参数里面
        :param key: 需要保存的json值的键
        :param p: 保存后的参数名
        :return: 无
        """
        self.json[p] = self.jsonres[key]

    def __get_value(self,p):
        # 用{key}的形式去替换参数里面的字符串，如没有就不会替换
        for key in self.json.keys():
            p = p.replace('{' + key + '}', self.json[key])
        return p

