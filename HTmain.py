import twilio_stuff.py

def main():
  dict = {}
  n=0
  while n==0:
	  if dict.has_key(usr_phone_number_str) == False:
	    send_message(START_MSGS[0], usr_phone_number_str, from_number)
	    incoming_texts = get_message_by_user_number(usr_phone_number_str)
	    #user_dict = {'phone_num':usr_phone_number_str, 'responses':incoming_texts} 
	    #dict.update(user_dict)
	    new_incoming_texts = get_message_by_user_number(usr_phone_number_str)
	    while new_incoming_texts == incoming_texts:
	      new_incoming_texts = get_message_by_user_number(usr_phone_number_str)
	    incoming_texts = new_incoming_texts
	    if incoming_texts[1]:
	      send_message(START_MSGS[1], usr_phone_number_str, from_number)
	    new_incoming_texts = get_message_by_user_number(usr_phone_number_str)
	    while new_incoming_texts == incoming_texts:
	      new_incoming_texts = get_message_by_user_number(usr_phone_number_str)
	    incoming_texts = new_incoming_texts
	    if incoming_texts[2]:
	      send_message(START_MSGS[2], usr_phone_number_str, from_number)
	  else:
            for i in range(3):
		    incoming_texts = get_numeric_messages(usr_phone_number_str)
		    user_dict = {'phone_num':usr_phone_number_str, 'responses':incoming_texts} 
		    dict.update(user_dict)
            n=1         
