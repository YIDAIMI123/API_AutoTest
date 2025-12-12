import requests

class RequestsUtil: #请求基类
    session = requests.session()
    @staticmethod
    def send_request(**kwargs):
        # total_params = {
        #     "application": "web",
        #     "application_client_type": "pc",
        # }
        for key,value in kwargs.items():
            # if key == "params":
            #     params = kwargs.get("params", {})
            #     params.update(total_params) #字典中的update方法，如果键值不存在则会新增，如果键值已存在，则会覆盖原值
            #     kwargs["params"] = params
            if key == "file":
                for file_key, file_value in value.items():
                        value[file_key] = open(file_value, "rb")    #这里是将原来的文件路径字符串用文件对象替换（在字典里面是字符串）
        
        response = RequestsUtil.session.request(**kwargs)
        return response
