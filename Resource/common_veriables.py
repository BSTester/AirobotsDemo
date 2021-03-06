import os

# 公共变量

db_host = 'localhost' 
db_port = 5432 
db_user = 'postgres'
db_passwd = '123456'
db_name = '' 

redis_host = ''
redis_port = 6379
redis_passwd = ''

test_host = ''
test_php_host = ''

redis_ssh_host = ''
redis_ssh_port = 22
redis_ssh_user = ''
redis_ssh_key = os.path.join(os.path.dirname(__file__), 'TestFiles', 'develop.pem')

browser = 'Chrome'    # 启动浏览器类型，可选：Firefox、Chrome、PhantomJS
remote_url = 'http://grid:4444/wd/hub'

