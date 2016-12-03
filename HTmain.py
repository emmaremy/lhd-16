def main():
  msg_old_total = num_total_messages()
  if '''latest message''' == 'Hello':
    output = 'Welcome to HealthTexts! What should we ask you when we check in?'
  msg_new_total = num_total_message()  
  while msg_new_total != msg_old_total:
    diff = msg_new_total - msg_old_total 
    for i in range(diff):
      if (msg_old_total+i)%2 == 0:  
        question = messages[msg_old_total+i]
        output = 'What time during the day should we check in?'
      if (msg_old_total+i)%2 != 0:
        time = messages[msg_old_total+i]
        output = 'Okay, text you later'
    msg_old_total = msg_new_total
    msg_new_total = num_total_messages()
     
