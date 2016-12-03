import matplotlib.pyplot as plt
import pandas
# from automated-survey-django-master.automated_survey import models

class result_plots:
    # will need to import questions class and get rid of this stuff
    TEXT = 'text'
    YES_NO = 'yes-no'
    NUMERIC = 'numeric'

    QUESTION_KIND_CHOICES = (
        (TEXT, 'Text'), 
        (YES_NO, 'Yes or no'), 
        (NUMERIC, 'Numeric')
    )

    def __init__(self, question_kind, question_body, answer_data):
	self.question_kind = question_kind
	self.question_body = question_body
	# this will likely have to change when we figure out what format 
	# the question data will actually be in by default, but for now
	# will assume it comes in a list of QuestionResponse dictionaries
	self.answer_data = answer_data
	
    def plot_data(question_kind, answer_data):
	if question_kind not in [cls.YES_NO, cls.NUMERIC, cls.TEXT]:
	    raise TypeError("requested to graph question with invalid type")

	if question_kind == TEXT:
	    raise TypeError("requested graph of question with text answer")

	self.timestamps = [answer[time] for answer in self.answer_data]
	self.data = [answer[response] for answer in self.answer_data]

	if self.question_kind == cls.YES_NO:
	    pass

	if self.question_kind == cls.NUMERIC:
	    pass

    def _numeric_plot(self):
	# TODO: add title and possibly legend
	plt.plot(self.timestamps, self.data)
 
