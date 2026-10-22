import datetime

from langchain_core.tools import tool




#定义智能体本地工具
@tool
def get_current_time()->str:
    '''获取当前系统时间，返回一个时间字符串'''
    return str(datetime.datetime.now())

@tool
def calculator(a:float,b:float,opt:str) ->str:
    '''数字计算工具，支持 + - * / 运算'''
    if opt == "+":
        return a + b
    elif opt == "-":
        return a - b
    elif opt == "*":
        return a * b
    elif opt == "/":
        return a / b
    return "不支持该运算方式"

tools = [get_current_time,calculator]