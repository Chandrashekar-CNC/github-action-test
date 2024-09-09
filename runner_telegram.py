import platform
import requests, random, os
from datetime import datetime
import pytz
import tzlocal


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
sendMessage("test from github action")



# Get the server's local timezone
local_tz = tzlocal.get_localzone()

# Get the current time in the server's local timezone
server_time = datetime.now(local_tz)

# Print the server's timezone and current date and time
x = f"Server Timezone: {local_tz}\n\n"
x += f"Server Date and Time: {server_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"

# Convert the server time to Indian Standard Time (IST)
ist_tz = pytz.timezone('Asia/Kolkata')
ist_time = server_time.astimezone(ist_tz)

# Print the date and time in IST
x += f"Indian Standard Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
sendMessage(str(x))


y = "Runner Information:\n\n"
y += f"Operating System: {platform.system()}\n\n"
y += f"OS Version: {platform.release()}\n\n"
y += f"Machine Type: {platform.machine()}\n\n"
sendMessage(str(y))

# Get environment variables from GitHub Actions
event_name = os.getenv('GITHUB_EVENT_NAME')
workflow = os.getenv('GITHUB_WORKFLOW')
runner_name = os.getenv('RUNNER_NAME')
job_name = os.getenv('GITHUB_JOB')
trigger = os.getenv('GITHUB_EVENT_PATH')

z = "GitHub Action Environment:\n\n"
z += f"Event: {event_name}\n\n"
z += f"Workflow: {workflow}\n\n"
z += f"Runner: {runner_name}\n\n"
z += f"Job: {job_name}\n\n"
z += f"Trigger file path: {trigger}\n\n"

z += f"\nCurrent Time: {datetime.now()}\n\n"
sendMessage(str(z))
