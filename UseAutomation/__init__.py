import time
import autoit
import pynput
import uiautomation


# 参数配置
admin_list = [
    {
        "user": "duliguo",
        "username": "admin",
        "password": "Smbtest00",
    },
    {
        "user": "luxiao",
        "username": "lx",
        "password": "Smbtest00",
    },
]

device_list = [
    {},
    {},
    {},
    {},
    {},
]

person_list = [
    {},
    {},
    {},
    {},
    {},
    {},
]

access_list = [
    {},
    {},
    {},
    {},
    {},
    {},
]

# 路径配置
PATH = ""
EZAccessClientPath = ""
EZAccessServerPath = ""
OutPutPath = ""