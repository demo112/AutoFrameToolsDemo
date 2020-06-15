from UseAutomation.controlOperation import *

co = ControlOperation()


# 业务方法
def send_user_name(username, Name="用户名", Depth=9, foundIndex=1):
    try:
        flag = uiautomation.EditControl(Name=Name, Depth=Depth, foundIndex=foundIndex)
        flag = co.give_value(flag, username)
        print(1, flag.GetValuePattern().Value)
    except Exception as e:
        print("Can not control EZAccess, because: %s" % e)


def send_password(pwd, Name="密码", Depth=9, foundIndex=2):
    try:
        flag = uiautomation.EditControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
        flag = co.give_value(flag, pwd)
        print(1, flag.GetValuePattern().Value)
    except Exception as e:
        print("Can not control EZAccess, because: %s" % e)


def device_contorl(Name="设备管理", Depth=12, foundIndex=2):
    """
    选择设备管理页签
    :param Name: 标签元素名称
    :param Depth: 空间深度
    :param foundIndex: 同种类控件序列号
    :return: 页签控件
    """
    try:
        flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
        flag.Click()
        return flag

    except Exception as e:
        print("Can not control EZAccess, because: %s" % e)


def login(username, password):
    send_user_name(username)
    send_password(password)


if __name__ == '__main__':
    login("admin", "Smbtest00")
    # device_contorl(Name="设备管理", Depth=12, foundIndex=2)
