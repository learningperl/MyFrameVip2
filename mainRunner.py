# coding:utf8
from common.Excel import Reader, Writer
from inter.httpkeys import HTTP
import inspect
from common import logger,config
from common.mysql import Mysql
from common.mail import Mail


def runCases(http, line):
    """
    执行每一行用例的方法
    :param line: 参数列表
    :return: 无
    """
    if len(line[0]) > 0 or len(line[1]) > 0:
        # 分组信息不用执行
        pass
    else:
        func = getattr(http, line[3])
        p = inspect.getfullargspec(func).__str__()
        p = p[p.find('args=') + 5:p.find(', varargs')]
        p = eval(p)
        p.remove('self')

        if len(p) == 0:
            func()
        elif len(p) == 1:
            func(line[4])
        elif len(p) == 2:
            func(line[4], line[5])
        elif len(p) == 3:
            func(line[4], line[5], line[6])
        else:
            logger.warn("框架暂时只支持3个参数！")


if __name__ == "__main__":
    logger.info("整个框架使用该入口执行")

    # 运行用例之前，初始化配置，初始化数据库
    config.get_config('./lib/conf.properties')
    mysql = Mysql()
    mysql.init_mysql('./lib/userinfo.sql')

    # 开的读取用例
    reader = Reader()
    reader.open_excel('./lib/HTTP.xls')
    sheetname = reader.get_sheets()
    logger.info(sheetname)

    writer = Writer()
    writer.copy_open('./lib/HTTP.xls', './lib/result-HTTP.xls')

    http = HTTP(writer)

    for sheet in sheetname:
        # 设置当前读取的sheet页面
        reader.set_sheet(sheet)
        writer.set_sheet(sheet)
        writer.clo = 7

        for i in range(reader.rows):
            writer.row = i
            line = reader.readline()
            # 执行用例的方法
            logger.info(line)
            try:
                runCases(http, line)
            except Exception as e:
                logger.exception(e)

    writer.save_close()

    mail = Mail()
    mail.send(config.config['mailtxt'])