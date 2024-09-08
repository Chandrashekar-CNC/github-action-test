
import requests, random, os
#, pytz, subprocess
#from internetarchive import upload

token = os.environ.get('FORMER_RADIO_BOT')
log_token = os.environ.get('CHATHUR_BOT')
channel_id = os.environ.get('KISANVANI_CH_ID')
log_channel_id = os.environ.get('CNC_CH_ID')
accessKey = os.environ.get('access_key')
secretKey = os.environ.get('secret_key')

def sendMessage(text):
    furl = "https://api.telegram.org/bot"+log_token+"/sendMessage"
    mydata = { 'chat_id':log_channel_id, 'text':text, 'parse_mode':'HTML', 'disable_notification':'TRUE' }
    while True:
        r = requests.get(furl,data=mydata).json()
        if str(r['ok']) == "True":
            print("message_id",r['result']['message_id'])
            return r['result']['message_id']
        if str(r['error_code']) == str(429):
            print("Send Bot Busy, Sleeping for ",r['parameters']['retry_after'],"Seconds")
            time.sleep(int(r['parameters']['retry_after']))
        else:
            print("Send Message err",r)
            return "\nSend Message Err\n"+str(r)
            break
sendMessage("test from github ci/co action at 6:50pm")
