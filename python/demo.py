def fun():
    name = 'tome'
    print(f'有参数={name}')


def fun_1():
    print('无参数')


def ret():
    he = 'True'
    if he == "True":
        print("True")
    else:
        return 1


def ret_1():
    print("无返回值")

fun()
fun_1()
ret()
ret_1()
