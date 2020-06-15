# 该文件主要放置基础操作方法：如点击、赋值、编辑、选择等


from UseAutomation.__init__ import *


class ControlOperation:
    """
    客户端具体操作方法类，
    如：
    多选框勾选；
    文本框编辑、删除、赋值；
    等
    """

    def __init__(self):
        pass

    # 操作方法
    def give_value(self, target, value):
        """
        为查找到的元素赋值
        :param target: 目标元素
        :param value: 需要赋的值
        :return: 已赋值的对象
        """
        value = str(value)
        try:
            target.Click()
            pynput.keyboard.Controller().type(value + "\n")
            time.sleep(.6)
        except Exception as e:
            print("【%s】赋值【%s】失败，请处理！" % (target.Name, value))
            print("原因：",e)
        return target
