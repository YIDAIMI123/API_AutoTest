import yaml
import os
# from data import ex

# def write_yaml(data):
#     with open("ex.yaml","w") as f:
#         yaml.dump(data,f,allow_unicode=True)

# def read_yaml(key):
#     with open("ex.yaml", "r") as f:
#         result = yaml.safe_load(f)
#         return result[key]
    
# # 清空yaml文件内容
# def clean_yaml():
#     with open("ex.yaml", mode="w", encoding="utf-8") as f:
#         pass

# #测试用例中读取yaml，以实现数据驱动
# def read_yaml_testcase(yaml_path):
#     with open(yaml_path, "r", encoding="utf-8") as f:
#         result = yaml.safe_load(f)
#         return result
    

#上述写法是只能针对一个yaml文件进行读取和写入，下面的是针对多个yaml文件进行读取和写入

class YamlUtil:

    @staticmethod
    def read_yaml(path,key):
        with open(path, "r", encoding="utf-8") as f:
            result = yaml.safe_load(f)
            return result[key]

    @staticmethod
    def write_yaml(path, data): #此处的data是字典数据，不单单是值，是键值对
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True)

    @staticmethod
    def clean_yaml(path):
        with open(path, mode="w", encoding="utf-8") as f:
            pass
    
    @staticmethod
    def read_yaml_testcase(yaml_path):
        """适用于获取 token 等变量"""
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data


    