import twilio_private_stuff as tw
import json

def get_messages_by_user_number(usr_phone_number_str):
    # get a list of all the sms messages
    smss = tw.client.sms.messages.list()
    print smss
    return
    smss = json.loads(smss)    
    # list of dictionaries containing data for each sms message
    actual_message_data = smss['sms_messages']
    messages_from_usr = [message['body'] for message in actual_message_data]
    print messages_from_usr
    return messages_from_usr

get_messages_by_user_number('+16152759927')


def send_message(msg_str, usr_phone_number_str='+16152759927', from_number='+16156452860'):
    tw.client.messages.create(to=usr_phone_number_str, from_ = from_number, body=msg_str)

send_message('test')
