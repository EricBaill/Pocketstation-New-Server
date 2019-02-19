
1.开启服务器：
python manager.py runserver

2.需要清理openid的时候，找到右侧user表或者admin表 删除即可
























1.导入依赖包：执行命令：
pip install -r requirements.txt


2.数据库迁移：
1).python manager.py db init
2).python manager.py db migrate
3).python manager.py db upgrade