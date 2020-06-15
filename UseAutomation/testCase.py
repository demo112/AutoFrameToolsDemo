# 该文件主要放置具体的测试用例, 如：点击考勤统计，点击考勤明细，查询昨天记录并导出
from UseAutomation.uiControl import *


class Staibilities:
    """
    稳定性
    """

    def __init__(self):
        pass


class Pressure:
    """
    压力
    """

    def __init__(self):
        pass


class Daily:
    """
    日常
    """

    def __init__(self):
        pass

    def login(self, username, password):
        lg = ControlClint()
        lg.send_user_name(username)
        lg.send_password(password)


class UI:
    def __init__(self):
        pass

    def change_tab(self):
        de = DeviceControl()
        pe = PersonControl()
        ac = AccessControl()
        at = AttendanceControl()
        de.tab_device(Name="设备管理", Depth=12, foundIndex=2)
        pe.tab_person(Name="人员管理", Depth=12, foundIndex=3)
        ac.tab_access(Name="访问控制", Depth=12, foundIndex=4)
        at.tab_attendence(Name="考勤管理", Depth=12, foundIndex=4)


if __name__ == '__main__':
    ui = UI()
    daily = Daily()
    daily.login("admin", "Smbtest00")
    ui.change_tab()
