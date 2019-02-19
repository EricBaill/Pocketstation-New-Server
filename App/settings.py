def get_database_uri(DATABASE):
    dialect = DATABASE.get('dialect') or 'mysql'
    mysql = DATABASE.get('mysql') or 'pymysql'
    username = DATABASE.get('username') or 'root'
    password = DATABASE.get('password') or '123456'
    host = DATABASE.get('host') or 'localhost'
    port = DATABASE.get('port') or '3306'
    db = DATABASE.get('db') or 'bbruan'
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,mysql,username,password,host,port,db)


class Config():
    TEST = False
    DEBUG = False

    WX_APP_ID = "wxc7cf4e85ecbf8282"
    WX_APP_SECRET = "bafb0339afa3db639000a92ae15ff072"

    SECRET_KEY = '110'
    # SESSION_TYPE = 'redis'
    SQLALCHEMY_TRACK_MODIFICATIONS=True

class DevelopConfing(Config):
    DEBUG = True
    DATABASE = {
        'dialect':'mysql',
        'mysql':'pymysql',
        'username':'root',
        'password':'123456',
        'host':'localhost',
        'port':'3306',
        'db':'bbruan',
        'OPTIONS':{
            'init_command':"SET foreign_key_checks = 0"
        }
    }
    SQLALCHEMY_DATABASE_URI=get_database_uri(DATABASE)

env = {
    'develop':DevelopConfing
}