#coding='utf-8'

#通用的方法
def try_int(arg,default):
    try:
        arg=int(arg)
    except Exception as e:
        arg=default
    return arg