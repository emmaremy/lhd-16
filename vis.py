import matplotlib.pyplot as plt
import pandas
# may want to use numpy later for its arrays and such
# import numpy as np

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

    def __init__(self, question_body, data, timestamps, question_kind=self.NUMERIC):
	self.question_kind = question_kind
	self.question_body = question_body
	self.data = data
	self.timestamps = timestamps
	
    def plot_data(self):
	if self.question_kind not in [self.YES_NO, self.NUMERIC, self.TEXT]:
	    raise TypeError("requested to graph question with invalid type")

	if self.question_kind == self.TEXT:
	    raise TypeError("requested graph of question with text answer")

	if self.question_kind == self.YES_NO:
	    pass

	if self.question_kind == self.NUMERIC:
	    self._numeric_plot()

    def _numeric_plot(self):
	# TODO: add title and possibly legend
	plt.plot(self.timestamps, self.data)
	
	plt.savefig('test.png')


def plot(timestamps, data):
    plt.plot(self.timestamps, self.data)
    plt.save('report.png')
