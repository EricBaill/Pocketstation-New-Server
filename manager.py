from flask_migrate import MigrateCommand
from flask_script import Manager
from App import create_app

app = create_app('develop')

manager = Manager(app=app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':

    # manager.run()
    app.run(host='0.0.0.0',port='5000' )
