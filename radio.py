#
# FFMPEG
import concurrent.futures, subprocess
import requests, random, pytz, subprocess
import datetime, os, time, sys, textwrap
from internetarchive import upload
from fpdf import FPDF

token = os.environ.get('FORMER_RADIO_BOT')
log_token = os.environ.get('CHATHUR_BOT')
channel_id = os.environ.get('KISANVANI_CH_ID')
log_channel_id = os.environ.get('CNC_CH_ID')
accessKey = os.environ.get('access_key')
secretKey = os.environ.get('secret_key')


city = {}
#city["city name"] = ["frequency","url_no","output file","city name in kannada","city name in english","serial number","metadata"]
city["hsn"] = ["FM102.2", "172/", "Hassan/" + datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " HASSAN.mp3","ಹಾಸನ","Hassan","13"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+ datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಹಾಸನ"+"' -metadata author='ಆಕಾಶವಾಣಿ ಹಾಸನ' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["bad"] = ["FM103.5", "211/", "Bhadravati/" + datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " BHADRAVATI.mp3","ಭದ್ರಾವತಿ","Bhadravati","12"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+ datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಭದ್ರಾವತಿ"+"' -metadata author='ಆಕಾಶವಾಣಿ ಭದ್ರಾವತಿ' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["ban"] = ["MW612Kz", "030/", "Bangalore/" + datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " BANGALORE.mp3","ಬೆಂಗಳೂರು","Bangalore","11"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+ datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಬೆಂಗಳೂರು"+"' -metadata author='ಆಕಾಶವಾಣಿ ಬೆಂಗಳೂರು' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]

#10 City
city["mys"] = ["FM100.6", "177/", "Mysore/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " MYSORE.mp3","ಮೈಸೂರು","Mysore","01"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಮೈಸೂರು"+"' -metadata author='ಆಕಾಶವಾಣಿ ಮೈಸೂರು' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["man"] = ["FM100.3", "073/", "Mangalore/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " MANGALORE.mp3","ಮಂಗಳೂರು","Mangalore","02"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಮಂಗಳೂರು"+"' -metadata author='ಆಕಾಶವಾಣಿ ಮಂಗಳೂರು' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["mad"] = ["FM103.1", "068/", "Madikeri/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " MADIKERI.mp3","ಮಡಿಕೇರಿ","Madikeri","03"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಮಡಿಕೇರಿ"+"' -metadata author='ಆಕಾಶವಾಣಿ ಮಡಿಕೇರಿ' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["rai"] = ["FM102.1", "198/", "Raichur/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " RAICHUR.mp3","ರಾಯಚೂರು","Raichur","04"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ರಾಯಚೂರು"+"' -metadata author='ಆಕಾಶವಾಣಿ ರಾಯಚೂರು' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["vij"] = ["FM101.8", "145/", "Vijayapura/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " VIJAYAPURA.mp3","ವಿಜಯಪುರ","Vijayapura","05"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ವಿಜಯಪುರ"+"' -metadata author='ಆಕಾಶವಾಣಿ ವಿಜಯಪುರ' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["kal"] = ["FM103.7", "015/", "Kalaburagi/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " KALABURGI.mp3","ಕಲಬುರಗಿ","Kalaburagi","06"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಕಲಬುರಗಿ"+"' -metadata author='ಆಕಾಶವಾಣಿ ಕಲಬುರಗಿ' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["chi"] = ["FM102.6", "105/", "Chitradurga/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " CHITRADURGA.mp3","ಚಿತ್ರದುರ್ಗ","Chitradurga","07"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಚಿತ್ರದುರ್ಗ"+"' -metadata author='ಆಕಾಶವಾಣಿ ಚಿತ್ರದುರ್ಗ' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["kar"] = ["FM102.3", "123/", "Karwar/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " KARWAR.mp3","ಕಾರವಾರ","Karwar","08"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಕಾರವಾರ"+"' -metadata author='ಆಕಾಶವಾಣಿ ಕಾರವಾರ' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["hos"] = ["FM100.5", "184/", "Hospet/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " HOSPET.mp3","ಹೊಸಪೇಟೆ","Hospet","09"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಹೊಸಪೇಟೆ"+"' -metadata author='ಆಕಾಶವಾಣಿ ಹೊಸಪೇಟೆ' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
city["dar"] = ["FM103.0", "150/", "Dharwad/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " DHARWAD.mp3","ಧಾರವಾಡ","Dharwad","10"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಧಾರವಾಡ"+"' -metadata author='ಆಕಾಶವಾಣಿ ಧಾರವಾಡ' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]

#Akashvani Bellari
#city["bel"] = ["FM103.0", "150/", "Bellari/" +  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " Bellari.mp3","ಬಳ್ಳಾರಿ","Bellari","11"," -metadata album_artist='ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ' -metadata title='"+  datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y") + " ಬಳ್ಳಾರಿ"+"' -metadata author='ಆಕಾಶವಾಣಿ ಬಳ್ಳಾರಿ' -metadata album='ಕಿಸಾನ್ ವಾಣಿ' -metadata year='"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y")+"' "]
#http://air.pc.cdn.bitgravity.com/air/live/pbaudio142/playlist.m3u8

city3 = ["bad"]
city10 = ["bad","hsn","ban","mys","man","mad","rai","vij","kal","chi","kar","hos","dar"]
cityAll = ["hsn","ban","bad","mys","man","mad","rai","vij","kal","chi","kar","hos","dar"]

def sendTelegram(rec):
    if not os.path.exists(city[rec][2]):
        print("File Not Found")
        sendMessage(city[rec][3]+"\nA_Tegr File Not Found")
        return city[rec][2]+"\nA_Tegr File Not Found"

    time.sleep(int(city[rec][5]))
    furl = "https://api.telegram.org/bot"+token+"/sendAudio"
    mydata = { 'chat_id':channel_id,
                'title': datetime.datetime.now().strftime("%Y-%m-%d ")+ city[rec][0],
                'caption':city[rec][3],
                'performer':'ಕಿಸಾನ್ ವಾಣಿ '+city[rec][3],
                'parse_mode':'HTML' }
    filess = { 'audio':open(city[rec][2],'rb'),'thumb':open('img/ka.jpg','rb') }
    while True:
        r = requests.get(furl,data=mydata,files=filess).json()
        if str(r['ok']) == "True":
            print(city[rec][3]," A_Telegram Sent ",r['ok'])
            return city[rec][3]+" A_Telegram Sent "+str(r['ok'])
        if str(r['error_code']) == str(429):
            print("Send A_telegram Busy, Sleeping for ",r['parameters']['retry_after'],"Seconds")
            time.sleep(int(r['parameters']['retry_after']))
        else:
            print("Telegram Send err :",r)
            #files.download(city[rec][2])
            sendMessage(city[rec][3]+"\nA_Telegram Send Err\n Message :\n"+str(r))
            return "A_Telegram Send err :"+str(r)

def createDirs(citys):
    for c in citys:
        if not os.path.exists(city[c][4]):
            os.makedirs(city[c][4])
            print("Creating Folder " + city[c][4])
        else:
            print(city[c][4] + " ok" )
    if not os.path.exists("img"):
        print("Creating Folder img")
        os.makedirs("img")
    if not os.path.exists("img/ka.jpg"):
        print("Downloading img/ka.jpg")
        #os.system("wget -O img/ka.jpg https://chandrashekarcn.github.io/img/ka.jpg")
        r = requests.get("https://chandrashekarcn.github.io/img/ka.jpg")
        with open("img/ka.jpg", "wb") as f:
            f.write(r.content)

def clearDirs(citys):
    for c in citys:
        os.system("rm -fr " + city[c][4] )

def sendDoc(doc):
    # general files up to 50mb
    furl = "https://api.telegram.org/bot"+log_token+"/sendDocument"
    mydata = { 'chat_id':log_channel_id,'caption':'Log Files'}
    files = { 'document':open(doc,'rb'),'thumb':open('img/ka.jpg','rb')}
    while True:
        r = requests.get(furl,data=mydata,files=files).json()
        if str(r['ok']) == "True":
            print("Document message_id",r['result']['message_id'])
            return r['result']['message_id']
        if str(r['error_code']) == str(429):
            print("Document Send Bot Busy, Sleeping for ",r['parameters']['retry_after'],"Seconds")
            time.sleep(int(r['parameters']['retry_after']))
        else:
            print("Send Message err",r)
            return "\nSend Message Err\n"+str(r)
            break

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

def editMessage(id,text):
    furl = "https://api.telegram.org/bot"+log_token+"/editMessageText"
    mydata = { 'chat_id':log_channel_id, 'message_id':id, 'text':text, 'parse_mode':'HTML', 'disable_notification':'TRUE' }
    while True:
        r = requests.get(furl,data=mydata).json()
        if str(r['ok']) == "True":
            print(id,"Edit Message : ",r['ok'])
            return "\n"+str(id)+" Edit Message : "+str(r['ok'])
            break
        if str(r['error_code']) == str(429):
            print(id,"Edit Bot Busy, Sleeping for ",r['parameters']['retry_after'],"Seconds")
            time.sleep(int(r['parameters']['retry_after']))
        else:
            print(id,"Edit Message err ",r)
            return "\n"+str(id)+" Edit Message Err \n"+str(r)
            break

def ffmpegRecord(rec,hh,mm,archive):
    #time.sleep(int(city[rec][5]))
    url = '"https://air.pc.cdn.bitgravity.com/air/live/pbaudio' + city[rec][1] + 'playlist.m3u8"'

    #Banglore url changed from rest
    if (rec == "ban"):
        url = 'https://airhlspush.pc.cdn.bitgravity.com/httppush/hlspbaudio030/hlspbaudio03032kbps.m3u8'

    msg = "From OPPO Mobile A57\n"+city[rec][3]+"\nRec Up To: "+str(hh)+":"+str(mm)
    log = "\n\n********** "+city[rec][3]+" **********\nRec Up To: "+str(hh)+":"+str(mm)
    if (len([1 for x in list(os.scandir(city[rec][4])) if x.is_file()]) > 0):
        #print("Clearing old files ...Done")
        log += "\n\nClearing Old Files... \nDone..."
        msg += "\n\nClearing old files ...Done"
        os.system("rm "+city[rec][4]+"/*")

    #print("\n*****Future Time****")
    know = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y "+str(hh)+":"+str(mm)+":00")
    #print("\nFuture Time = ",know)
    log += "\n\nFuture  Time = "+know
    msg += "\n\n"+know

    #print("\n*****Present Time****")
    #print("Current Time = "+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y %H:%M:%S"))
    log += "\nCurrent Time = "+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y %H:%M:%S")
    msg += "\n"+datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y %H:%M:%S")

    #Future timestamp
    element = datetime.datetime.strptime(know,"%d-%B-%Y %H:%M:%S")
    e_stamp = int(datetime.datetime.timestamp(element))
    #print("\nFuture  Timestamp  = ",e_stamp)
    log += "\n\nFuture  TimeStamp = "+str(e_stamp)
    msg += "\n\n"+str(e_stamp)

    #Current timestamp
    sknow = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y %H:%M:%S")
    selement = datetime.datetime.strptime(sknow,"%d-%B-%Y %H:%M:%S")
    s_stamp = int(datetime.datetime.timestamp(selement))
    #print("Current Timestamp  = ",s_stamp)
    log += "\nCurrent TimeStamp = "+str(s_stamp)
    msg += "\n"+str(s_stamp)

    #Diff in seconds
    #print("\nDifference In Seconds = ",e_stamp-s_stamp)
    t = time.gmtime(e_stamp-s_stamp)
    #print("Difference In Time = ",str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec))
    log += "\n\nDifference In Seconds = "+str(e_stamp-s_stamp)
    log += "\nDifference In Time = "+str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec)
    msg += "\n\nDifference In Seconds = "+str(e_stamp-s_stamp)
    msg += "\nDifference In Time = "+str(t.tm_hour)+":"+str(t.tm_min)+":"+str(t.tm_sec)

    rTime = (e_stamp-s_stamp)+60
    #print("Recording Time :",(e_stamp-s_stamp),"+ 30 =",rTime)
    log += "\nRecording Time "+str(e_stamp-s_stamp)+" +"+" 30 = "+str((e_stamp-s_stamp)+30)
    msg += "\nRec Time "+str(e_stamp-s_stamp)+" +"+" 30 = "+str((e_stamp-s_stamp)+30)

    m_id = sendMessage(msg)
    if(rTime <= 0):
        #print("\nNegative Seconds \nExit\n")
        log += "\n\nNegative Seconds\n\nExit\n"
        msg += "\n\nNegative Seconds\nExit\n"
        time.sleep(3)
        editMessage(m_id,msg)
        return log

    #print("\nRecord Started For",city[rec][4]+" FM","Duration "+str(rTime))
    log += "\n\nRecord Started For "+city[rec][4]+" FM Duration "+str(rTime)
    msg += "\n\nRecording Started"

    fileCount=0
    fileName = []
    count404 = 0
    time.sleep(1)
    editMessage(m_id,msg)

    # Record Loop
    while s_stamp < e_stamp:
        fileCount += 1
        cmd = 'ffmpeg  -i ' + url + ' -t ' + str(rTime-30) + city[rec][6] + city[rec][4]+"/"+str(fileCount)+".mp3 2>> "+city[rec][4]+"/"+city[rec][4]+"_err"
        log += "\n\n"+cmd
        os.system(cmd)
        #print(rec," End of ffmpeg cmd, record")
        log += "\n"+rec +" End Of FFMPEG CMD "

        if(os.path.exists(os.path.join(city[rec][4],str(fileCount)+".mp3"))):
            fileName.append(os.path.join(city[rec][4],str(fileCount)+".mp3"))

        if(check404(rec)=="True"):
            count404 += 1
            log += "\ncheck404 is True & count404 = "+str(count404)+" Sleeping For "+str(count404*60)+" Seconds"
            time.sleep(int(count404 * 60))

        sknow = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y %H:%M:%S")
        selement = datetime.datetime.strptime(sknow,"%d-%B-%Y %H:%M:%S")
        s_stamp = int(datetime.datetime.timestamp(selement))
        rTime = (e_stamp-s_stamp)+60

        if(s_stamp > e_stamp):
            #print("Recording Time Over, loop break")
            log += "\n\nRecording Time Over, [On Loop Break]"
            msg += "\nRecording Time Over\nLoop Break"
            break
        if(count404 > 5):
            #print(rec,"Too Much Err...  So breaking loop")
            log += "\n\nToo Much Error.... So Breaking Loop"
            msg += "\nToo Much Err...  So breaking loop"
            break
        #print("Next Recording File ",str(fileCount+1)+".mp3",rTime)
        log += "\nNext Recording File "+str(fileCount+1)+".mp3 "+str(rTime)

    #print("Recording Done.. \n\nRecorded Files")
    log += "\n\nRecording Done...\n\nRecorded Files\n"
    msg += "\nRecording Done...\n\nRecorded Files\n"

    cmd = ""
    if(len(fileName) >= 1):
        for f in fileName:
            #print(f)
            log += f + "\n"
            msg += f + "\n"
            cmd += f + "|"
    else:
        #print("No Files Recorded")
        log += "\n\nNo Files Recorded\nExit"
        msg += "\n\nNo Files Recorded\nExit"
        editMessage(m_id,msg)
        return log

    #print("\nPreparing MP3 File")
    log += "\n\nCreating Final MP3 File"
    msg += "\n\nCreating MP3 File"

    cmd = cmd[:-1]
    #cmd = 'ffmpeg -y -hide_banner -stats -loglevel 0 -i "concat:'+cmd+'" -acodec copy "'+city[rec][2]+'" 2>>'+rec+'_Final_Mp3_err'
    cmd = 'ffmpeg -y -i "concat:'+cmd+'" -acodec copy "'+city[rec][2]+'" 2>>'+city[rec][4]+'/mp3_err'    
    #print(cmd)
    log += "\n"+cmd
    os.system(cmd)
    #print("Done")
    log += "\nDone..."
    msg += "\nDone.."

    if (len([1 for x in list(os.scandir(city[rec][4])) if x.is_file()]) >1):
        #print("\nClearing small Files ...Done\n")
        log += "\n\nClearing Small Files...\nDone...\n"
        #for f in fileName:
            #os.system("rm "+f)
    Tmsg = ffprobe(rec)
    print("Check fname",city[rec][2])
    if os.path.exists(city[rec][2]):
        Tmsg += "\n\nRecorded File Ready"
        Tmsg += "\n\n" + sendTelegram(rec)
        if archive == "True":
            Tmsg += "\n" + archiveUpload(rec)
        if archive == "False":
            Tmsg += "\n" + "Archive args False"
        Tmsg += editMessage(m_id,msg+Tmsg+"\n\n******End Of Recording******")
        Tmsg += "\n\n**********End Of Recording**********"
        log += Tmsg
        return log
    else:
        Tmsg += "\n File Not Found\nSkipping Audio Send\n"
        Tmsg += editMessage(m_id,msg+Tmsg+"\n\n******End Of Recording******")
        Tmsg += "\n\n**********End Of Recording**********"
        log += Tmsg
        return log

def check404(rec):
    print(city[rec][3]," Checking For 404")
    url = "https://air.pc.cdn.bitgravity.com/air/live/pbaudio"+city[rec][1]+"playlist.m3u8"
    r = requests.get(url)
    if ((r.status_code == 404) or (r.status_code == 503)):
        print(city[rec][3]," Err Code ",r.status_code, " Sleeping For a Minute")
        time.sleep(30)
        return "True"
    else:
        print(city[rec][3]," check404() is ",r.status_code)
        return "False"

def ffprobe(rec):
    if os.path.exists(city[rec][2]):
        command = 'ffprobe "'+city[rec][2]+'"' +" 2>&1 | grep Duration | awk '{print $2}'"
        dur1 = subprocess.check_output(command,shell=True).decode("utf-8").strip()
        command = 'ffprobe "'+city[rec][2]+'"' +" 2>&1 | grep Stream | awk '{print $5,$6,$7,$8,$9,$10}'"
        dur = subprocess.check_output(command,shell=True).decode("utf-8").strip()
        command = 'ls -lh "'+city[rec][2]+'"'+" | awk '{print $5}' "
        size = subprocess.check_output(command,shell=True).decode("utf-8").strip()
        print(city[rec][5]+" "+city[rec][3]+" "+size+" "+dur1+" "+dur)
        return "\n\n"+city[rec][5]+" "+city[rec][3]+" "+size+" "+dur1+" \n"+dur
    else:
        print(city[rec][3]+" File Not Found")
        return "\n\n"+city[rec][3]+" File Not Found"

def waitUntil(hh,mm):
    #Future timestamp
    know = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y "+str(hh)+":"+str(mm)+":00")
    e_stamp = int(datetime.datetime.timestamp(datetime.datetime.strptime(know,"%d-%B-%Y %H:%M:%S")))
    print(know,"\nFuture  Timestamp = ",e_stamp)
    msg = "Recording will Start at\n"+know+"\n\nFuture  Timestamp = "+str(e_stamp) 
    #Current timestamp
    sknow = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y %H:%M:%S")
    selement = datetime.datetime.strptime(sknow,"%d-%B-%Y %H:%M:%S")
    s_stamp = int(datetime.datetime.timestamp(selement))
    print("Present Timestamp = ",s_stamp)
    msg += "\nPresent Timestamp = "+str(s_stamp)

    diff = e_stamp-s_stamp
    if (diff >= 0):
        print("Sleeping For [",e_stamp-s_stamp,"] Seconds")
        msg += "\n\nSleeping For [ "+str(e_stamp-s_stamp)+" ] Seconds..."
        m_id = sendMessage(msg)
        time.sleep(diff)
        print("Now",datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d-%B-%Y %H:%M:%S"))
        print("Thanks For Waiting")
        msg += "\nThanks For Waiting"
        editMessage(m_id,msg)
        return "True"
    else:
        print("You Are",diff,"Seconds Behind")
        msg += "\n\nYou Are "+str(diff)+" Seconds Behind"
        sendMessage(msg)
        return "False"

def archiveUpload(rec):
    if os.path.exists(city[rec][2]):
        r = upload('kissanvani2024', files=city[rec][2], verbose=True, access_key=accessKey, secret_key=secretKey)
        if str(r[0].status_code) == str(200):
            print("Archive "+city[rec][3]+" ",r[0].status_code)
            return "Archive "+city[rec][3]+" "+str(r[0].status_code)
        else:
            print("Archive Err "+city[rec][3]+" ",r[0].status_code)
            sendMessage("Archive Err "+city[rec][3]+" "+str(r[0].status_code))
            return "Archive Err "+city[rec][3]+" "+str(r[0].status_code)
    else:
        print(city[rec][2]," File Not Found For Archive Upload")
        return city[rec][2]+" File Not Found For Archive Upload"


def text_to_pdf(inputFileName, outputFileName):

    file = open(inputFileName)
    text = file.read().replace("ಬೆಂಗಳೂರು","Banglore").replace("ಹಾಸನ","Hassan").replace("ಭದ್ರಾವತಿ","Bhadravathi").replace("ಕಿಸಾನ್ ವಾಣಿ","Kisan Vani").replace("ಕೃಷಿ ಹಾಗು ರೈತರ ಕಲ್ಯಣ ಮಂತ್ರಲಯ","Ministry Of Agriculture And Farmer Welfare").replace("ಆಕಾಶವಾಣಿ","Akashvani").replace("ಮೈಸೂರು","Mysore").replace("ಮಂಗಳೂರು","Mangalore").replace("ಮಡಿಕೇರಿ","Madikeri").replace("ರಾಯಚೂರು","Raichur").replace("ವಿಜಯಪುರ","Vijayapura").replace("ಕಲಬುರಗಿ","Kalaburagi").replace("ಚಿತ್ರದುರ್ಗ","Chitradurga").replace("ಕಾರವಾರ","Karwar").replace("ಹೊಸಪೇಟೆ","Hospet").replace("ಧಾರವಾಡ","Dharwad")
    file.close()

    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        try:
            #print("line",line)
            lines = textwrap.wrap(line, width_text)
            #print("lines",lines)
        except Exception as e:
            lines = textwrap.wrap(str(e), width_text)
            #print("err",e)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)
    pdf.output(outputFileName, 'F')

#---------------------------------------------
# All Previous Recorded Files Will Be Deleted.
#clearFiles()
#---------------------------------------------
def record3city(hh,mm):
    print("**********Folders************")
    createDirs(city3)

    print("\n**********Total Citys**********")
    print("Selected Citys "+ str(len(city3)))

    print("\n*****Waiting For 5:30PM******")
    #wait_v1(17,30,1)
    waitUntil(17,30)

    print("\n******Recording Started************")

    hrs = []
    min = []
    arc = []

    for i in range(len(city3)):
        hrs.append(hh)
        min.append(mm)
        arc.append("True")

    hrs_tuple = tuple(hrs)
    min_tuple = tuple(min)
    arc_tuple = tuple(arc)

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(city3)) as executor:
        results = executor.map(ffmpegRecord,city3,hrs_tuple,min_tuple,arc_tuple)

    print("\n*************THE END*********")
    for r in results:
        with open('record.log', "a") as f:
            f.write(r)
        print(r)
    for r in city3:
        with open('record.log', "a") as f:
            f.write("\n"+ffprobe(r).replace("\n","")+"\n")
    with open('record.log',"a") as f:
        for r in city3:
            try:
                with open(city[r][4]+"/"+city[r][4]+"_err",'r') as ff:
                    f.write("\n\n************************ "+city[r][3]+" ************************\n\n")
                    f.write(ff.read())
                    f.write("\n\n************************ "+city[r][3]+" End*********************\n\n")
            except Exception as e:
                f.write(e)
    text_to_pdf("record.log","city3.pdf")
    sendDoc("city3.pdf")

def record10city(hh,mm):
    print("**********Folders************")
    createDirs(city10)

    print("\n**********Total Citys**********")
    print("Selected Citys "+ str(len(city10)))

    print("\n*****Waiting For 6:50PM******")
    #wait 18:50 (6:50)
    waitUntil(18,50)

    print("\n******Recording Started************")

    hrs = []
    min = []
    arc = []

    for i in range(len(city10)):
        hrs.append(hh)
        min.append(mm)
        arc.append("True")

    hrs_tuple = tuple(hrs)
    min_tuple = tuple(min)
    arc_tuple = tuple(arc)

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(city10)) as executor:
        results = executor.map(ffmpegRecord,city10,hrs_tuple,min_tuple,arc_tuple)

    print("\n*************THE END*********")
    for r in results:
        with open('record.log', "a") as f:
            f.write(r)
        print(r)
    for r in city10:
        with open('record.log', "a") as f:
            f.write("\n"+ffprobe(r).replace("\n","")+"\n")
    with open('record.log',"a") as f:
        for r in city10:
            try:
                with open(city[r][4]+"/"+city[r][4]+"_err",'r') as ff:
                    f.write("\n\n************************ "+city[r][3]+" ************************\n\n")
                    f.write(ff.read())
                    f.write("\n\n************************ "+city[r][3]+" End*********************\n\n")
            except Exception as e:
                f.write(e)
    text_to_pdf("record.log","city10.pdf")
    sendDoc("city10.pdf")

def recordMorning(hh,mm):
    print("**********Folders************")
    morning = ["hsn"]
    createDirs(morning)

    print("\n**********Total Citys**********")
    print("Selected Citys "+ str(len(morning)))

    print("\n*****Waiting For 6:40AM******")
    #wait(6:40)AM
    waitUntil(6,40)

    print("\n******Rec Started************")
    with open('record.log', "a") as f:
        f.write(ffmpegRecord(morning[0],hh,mm,"True"))
    print("\n*************THE END*********")

def recordCustom(hh,mm,rec,h,m):
    print("**********Folders************")
    custom = [rec]
    createDirs(custom)

    print("\n**********Total Citys**********")
    print("Selected Citys "+ str(len(custom)))

    print(f"\n*****Waiting Until {hh}:{mm}******\n")
    #wait(6:40)AM
    waitUntil(hh,mm)

    print("\n******Rec Started************")
    with open('record.log', "a") as f:
        f.write(ffmpegRecord(custom[0],h,m,"False"))
    with open('record.log', "a") as f:
        f.write("\n"+ffprobe(custom[0]).replace("\n","")+"\n")
    with open('record.log',"a") as f:
        with open(city[rec][4]+"/"+city[rec][4]+"_err",'r') as ff:
            f.write("\n\n************************ "+city[rec][3]+" ************************\n\n")
            f.write(ff.read())
            f.write("\n\n************************ "+city[rec][3]+" End*********************\n\n")
    print("\n*************THE END*********")
    os.system("rm city-"+rec)


#
#record3city(18,2)
#record10city(19,30)
#recordMorning(6,50)
#recordMorning(7,5)
#waitUntil(19,59)
#print("\n\n\n\t\t Program End ")



#check404("ban")
#ffmpegRecord(c,h,m)
#sendTelegram("hsn")
#archiveUpload("bad")

#print(len(sys.argv))
#print(sys.argv[0])

if len(sys.argv) > 1:
    if sys.argv[1] == "city3":
        print("City 3")
        record3city(18,2)

    elif sys.argv[1] == "city10":
        print("City 10")
        record10city(19,30)

    elif sys.argv[1] == "morning":
        print("Morning")
        recordMorning(7,5)

    elif sys.argv[1] == "custom":
        print("Custom")
        if len(sys.argv) == 7:
            print("7")
            if (isinstance(int(sys.argv[2]), int) and isinstance(int(sys.argv[3]), int) and isinstance(sys.argv[4], str) and isinstance(int(sys.argv[5]), int) and isinstance(int(sys.argv[6]), int)):
                if (int(sys.argv[2]) >= 0) and (int(sys.argv[2]) <= 24) and (int(sys.argv[3]) >= 0) and (int(sys.argv[3]) <= 59) and (int(sys.argv[5]) >= 0) and (int(sys.argv[5]) <= 24) and (int(sys.argv[6]) >= 0) and (int(sys.argv[6]) <= 59):
                    print("custom",sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
                    recordCustom(int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5]),int(sys.argv[6]))
                else:
                    print("Arg > 24 or < 0")
            else:
                print("int or str err custom",sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
        else:
            print("Missing argv")

    else:
        print("I Don't Know")


#
