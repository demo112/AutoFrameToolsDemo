# 该文件主要放置基本操作，如：点击切换页面，为某文本框赋值，删除某条记录等
from UseAutomation.controlOperation import *


class ControlClint:
    """
    客户端控制：除业务页签外的所有其他操作，登录、注销、修改密码、最大化、最小化、关闭等
    """

    def __init__(self):
        # 生成实例
        self.co = ControlOperation()

    def send_user_name(self, username, Name="用户名", Depth=9, foundIndex=1):
        try:
            flag = uiautomation.EditControl(Name=Name, Depth=Depth, foundIndex=foundIndex)
            flag = self.co.give_value(flag, username)
            print(1, flag.GetValuePattern().Value)
        except Exception as e:
            print("Can not control EZAccess, because: %s" % e)

    def send_password(self, pwd, Name="密码", Depth=9, foundIndex=2):
        try:
            flag = uiautomation.EditControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag = self.co.give_value(flag, pwd)
            print(1, flag.GetValuePattern().Value)
        except Exception as e:
            print("Can not control EZAccess, because: %s" % e)



class DeviceControl:
    """
    设备管理
    """

    def __init__(self):
        pass

    def tab_device(self, Name="设备管理", Depth=12, foundIndex=2):
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


class PersonControl:
    """
    人员管理
    """

    def __init__(self):
        pass

    def tab_person(self, Name="人员管理", Depth=12, foundIndex=3):
        """
        选择人员管理页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            print("Can not control EZAccess, because: %s" % e)


class AccessControl:
    """
    访问控制
    """

    def __init__(self):
        pass

    def tab_access(self, Name="访问控制", Depth=12, foundIndex=4):
        """
        选择人员管理页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            print("Can not control EZAccess, because: %s" % e)


class AttendanceControl:
    """
    考勤统计
    """

    def __init__(self):
        pass

    def tab_attendence(self, Name="考勤管理", Depth=12, foundIndex=4):
        """
        选择人员管理页签
        :param Name: 标签元素名称
        :param Depth: 空间深度
        :param foundIndex: 同种类控件序列号
        :return: 页签控件
        """
        try:
            flag = uiautomation.HyperlinkControl(Name=Name, Depth=Depth, fondIndex=foundIndex)
            flag.Click()
        except Exception as e:
            print("Can not control EZAccess, because: %s" % e)
