import twilio_private_stuff as tw
import json
#import parsexml


START_MSGS = ['Welcome to Health Texts! What should we ask you when we check in?',
	      'What time during the day should we check in?',
	      'Ok, text you later!',
              'Thanks! We recorded your response and will check in again tomorrow.']

def get_messages_by_user_number(usr_phone_number_str):
    # get a list of all the sms messages
    smss = tw.client.sms.messages.list()
    print smss
    smss = parsexml.xml_to_info(smss) 
    print smss 
    return
    # list of dictionaries containing data for each sms message
    actual_message_data = smss['sms_messages']
    messages_from_usr = [[message['body'], 
			  message['date_created']] for message in actual_message_data]
    print messages_from_usr
    return messages_from_usr

get_messages_by_user_number('+16152759927')


def send_message(msg_str, usr_phone_number_str='+16152759927', from_number='+16156452860'):
    tw.client.messages.create(to=usr_phone_number_str, from_ = from_number, body=msg_str)


def num_total_messages():
    return len(tw.client.messages.list()['sms_messages'])


def get_numeric_messages(usr_phone_number_str):
    messages_from_user = get_messages_by_user_number(usr_phone_number_str)
    data = []
    times = []
    for message in messages_from_users:
	try:
	    num = float(message[0])
	except ValueError:
	    return
	data.append(num)
	times.append(message[1])


# send_message('test')
