def main(path,args):
    try:
        if '/' in path[1:]:
            className = path[1:path.find('/',1)]
            funcName = path[path.find('/',1)+1:]
            print('class is %s and func is %s' % (className,funcName))
            eval(className+'().'+funcName+'()')
        elif len(path)==1:
            eval('index()')
        else:
            eval(path[1:]+'()')
    except NameError as e:pass
    except Exception as e:
        print('拦截器错误')
        pass