import os
import htmlPy
from PyQt4 import QtGui

#initial configuration

#we get the absolute path of the initialization script to manage all the assets and backend
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#GUI initialization
app = htmlPy.AppGUI(title=u"PepperPresenter Application")
app.maximized = True
#GUI configuration
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "template/")


#app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))

#Bind back end with front end
	#import functionalities
from back_end.BackEnd import PepperApp
	#register functionalities
app.bind(PepperApp(app))

app.template = ("index.html", {})
#run the app
if __name__ == "__main__":
	app.start()

