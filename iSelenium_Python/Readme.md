**Selenium 自动化测试程序（python版）**
运行环境：
- selenium web driver
- python3
- pytest
- git

配置文件：iselenium.ini
- 将配置文件复制到本地磁盘的[user.home目录
- 填入设置的chromedriver文件的全路径

运行命令：
pytest -v test/web_ut.py -o junit_family=xunit2 --junit-xml=pytests.xml