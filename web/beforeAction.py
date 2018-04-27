import tool
class test:
    def bbb(self):
        print('/test/bbb beforeAction')


def main(path,args):
    try:
        tool.runAction(path)
    except NameError as e:pass
    except Exception as e:
        print('拦截器错误')
        pass
    
