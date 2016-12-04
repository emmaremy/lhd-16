import datetime
import vis
import random

answer_data = []

now = datetime.datetime.now()
day_delta = datetime.timedelta(days=1)
for i in range(30):
   answer = {'time': now - i*day_delta,
	     'response': random.random()}
   answer_data.append(answer)

#results = vis.result_plots(vis.result_plots.NUMERIC, 'question', answer_data)

answer_data.plot_data()
