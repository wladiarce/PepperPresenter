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

	#functions are defined here, under the .Slot decoration
	@htmlPy.Slot(str, result=str)
	def start_presentation(self, json_data):
#read the json data from the form (ip, file, start)
		form_data = json.loads(json_data)
		my_path = form_data['file']
		my_ip = form_data['ip']
		start_slide = form_data['start']
		start_slide = int(start_slide)
		slide_number = 1

		slides_path = os.path.dirname(my_path) + '/slides/slide'
#initialize the presentation
		my_pres = Presentation(my_path)
		number_of_slides = len(my_pres.slides)
		notes = []
		#add:
		#tts = ALProxy("ALTextToSpeech", my_ip, 9559)
		self.app.evaluate_javascript("document.getElementById('presentation_image').style.display='block'")
		self.app.evaluate_javascript("document.getElementById('presentation_content').innerHTML = 'Log:<br>Starting presentation at: %s<br>Notes:'" %(my_path))

#loop over the slides
		for slide in my_pres.slides:
#add if slide_number >= start_slide
			slide_src = slides_path + str(slide_number) + '.jpg'
			self.app.evaluate_javascript("document.getElementById('slide').src = '%s'" %(slide_src))
			print('Showing slide ' + str(slide_number) +'. Source: '+ slide_src)
			if slide.has_notes_slide:
				notes_slide = slide.notes_slide
				text_frame = notes_slide.notes_text_frame
				for paragraph in text_frame.paragraphs:
					notes.append(paragraph.text)
					self.app.evaluate_javascript("document.getElementById('presentation_content').innerHTML += ' [%s]'" %(paragraph.text))

					print('Notes line of slide ' + str(slide_number) +': ' + paragraph.text)
					#add:
					#tts.say(paragraph.text)
#end if - add one to the slide
			slide_number +=1

#those 2 lines is only for check, comment them in the final app
		my_notes = ''.join(notes) 
		self.app.evaluate_javascript("document.getElementById('presentation_content').innerHTML += '<br>Presentation ended.'")
		return


#WORKING!

