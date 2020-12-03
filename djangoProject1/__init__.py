import pymysql

# 指定版本
pymysql.version_info = (1, 4, 13, "final", 0)
# 将mysql作为数据库引入
pymysql.install_as_MySQLdb()
