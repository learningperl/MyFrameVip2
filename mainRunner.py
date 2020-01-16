# coding:utf8
from common.Excel import Reader, Writer
from inter.httpkeys import HTTP
from inter.soapkeys import SOAP
import inspect,time
from common import logger,config
from common.mysql import Mysql
from common.mail import Mail
from common.excelresult import Res
from web.web import Web
from app.app import APP

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

    casename = 'HTTP.xls'

    # 运行用例之前，初始化配置，初始化数据库
    config.get_config('./lib/conf.properties')
    mysql = Mysql()
    mysql.init_mysql('./lib/userinfo.sql')

    # 开的读取用例
    reader = Reader()
    reader.open_excel('./lib/' + casename)
    sheetname = reader.get_sheets()
    logger.info(sheetname)

    writer = Writer()
    writer.copy_open('./lib/' + casename, './lib/结果-' + casename)

    t = str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

    writer.set_sheet(sheetname[0])
    writer.write(1,3,t)
    reader.readline()
    line = reader.readline()
    if line[1] == 'HTTP':
        http = HTTP(writer)
    elif line[1] == 'WEB':
        http = Web(writer)
    elif line[1] == "APP":
        http = APP(writer)
    else:
        http = SOAP(writer)

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

    writer.set_sheet(sheetname[0])
    t = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    writer.write(1, 4, t)

    writer.save_close()

    res = Res()
    result = res.get_res('./lib/结果-' + casename)

    mail = Mail()
    mail.mail_info['mail_subject'] = result['title']
    mailtext = config.config['mailtxt']
    mailtext = mailtext.replace('title',result['title'])
    mailtext = mailtext.replace('status', result['status'])
    mailtext = mailtext.replace('runtype', result['runtype'])
    mailtext = mailtext.replace('passrate', result['passrate'])
    mailtext = mailtext.replace('starttime', result['starttime'])
    mailtext = mailtext.replace('casecount', result['casecount'])
    mailtext = mailtext.replace('endtime', result['endtime'])
    if result['status'] == 'Fail':
        mailtext = mailtext.replace('#00d800', 'red')

    # 附件的路径，如果有多个就用,分割
    mail.mail_info['filepaths'] = ['./lib/结果-' + casename]
    mail.mail_info['filenames'] = ['结果-' + casename]

    mail.send(mailtext)