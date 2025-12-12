import pytest
import os
if __name__ == "__main__":
    # 运行 pytest，搜索当前目录及其子目录中的所有测试用例
    pytest.main()
    os.system("allure generate ./temp -c -o ./report")