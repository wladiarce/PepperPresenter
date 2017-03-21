#is not showing slides, only the last one

import htmlPy
import os
import json
from naoqi import ALProxy
from pptx import Presentation
import time

#linked class with front end
class PepperApp(htmlPy.Object):
	#GUI callable functions need to be in a class, inherited from htmlPy.Object and binded to the GUI
	def __init__(self, app):
		super(PepperApp, self).__init__()
		self.app = app
		self.my_path = ""
		self.my_ip = ""
		self.current_slide =""
		self.start_slide =""
		self.slides_path =""
		self.tts =""
		self.my_pres =""
		self.number_of_slides = ""

	#functions are defined here, under the .Slot decoration
	

	@htmlPy.Slot(str)
	def start_presentation(self, json_data): #initializes everything
#read the json data from the form (ip, file, start)
		form_data = json.loads(json_data)
		self.my_path = form_data['file']
		self.my_ip = form_data['ip']
		self.start_slide = form_data['start']
#initialize the presentation and variables
		self.start_slide = int(self.start_slide)
		self.current_slide = self.start_slide
		self.slides_path = os.path.dirname(self.my_path) + '/slides/slide'
		self.my_pres = Presentation(self.my_path)
		self.number_of_slides = len(self.my_pres.slides)
		notes = []
#connect to the robot and show initial slide
		#COMENT THIS WHEN TESTING OUTISDE ROBOT
		self.tts = ALProxy("ALAnimatedSpeech", str(self.my_ip), 9559)
		
		slide_src = self.slides_path + str(self.start_slide) + '.jpg'
		self.app.evaluate_javascript("document.getElementById('presentation_image').style.display='block'")
		self.app.evaluate_javascript("document.getElementById('presentation_content').innerHTML = 'Log:<br>Starting presentation at: %s<br>IP: %s<br>Notes:'" %(self.my_path, self.my_ip))
		self.app.evaluate_javascript("document.getElementById('slide').src = '%s'" %(slide_src))
		self.app.evaluate_javascript("document.getElementById('presentation_image').style.display = 'block'")
		print('Showing slide ' + str(self.current_slide) +'. Source: '+ slide_src)

		return


	@htmlPy.Slot()
	def present_slide(self):
#the slide is showing, so when you click on it it will read the notes of the slide
#if it is not the last one it will show the next slide, if it is the last one will elapse some time and close the image view
		slide = self.my_pres.slides[self.current_slide-1]
		if slide.has_notes_slide:
			notes_slide = slide.notes_slide
			text_frame = notes_slide.notes_text_frame
			for paragraph in text_frame.paragraphs:
				self.app.evaluate_javascript("document.getElementById('presentation_content').innerHTML += ' [%s]'" %(paragraph.text))
				print('Notes line of slide ' + str(self.current_slide) +': ' + paragraph.text)

				#COMENT THIS WHEN TESTING OUTISDE ROBOT
				self.tts.say(str(paragraph.text))
			
				time.sleep(1)
		self.current_slide +=1
		if self.current_slide <=self.number_of_slides:
			slide_src = self.slides_path + str(self.current_slide) + '.jpg'
			self.app.evaluate_javascript("document.getElementById('slide').src = '%s'" %(slide_src))
		else:
			time.sleep(2)
			self.app.evaluate_javascript("document.getElementById('presentation_image').style.display = 'none'")

		return

# #WORKING!

