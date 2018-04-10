from app import create_app
from flask_script import Manager, Server 
#Flask-Script is a command line parser for creating startup configurations.
# Manager initializes the flask script extension
# Server helps us launch the server
# Creating the app instance
app = create_app('development')

manager =  Manager(app)
manager.add_command('server',Server)



if __name__ == '__main__':
	manager.run()
