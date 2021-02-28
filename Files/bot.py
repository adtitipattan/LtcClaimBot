from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import *
from time import sleep
import json, re, os, requests, time

b = '\033[1;36m'
u = '\033[1;35m'
k = '\033[1;33m'
h = '\033[1;32m'
m = '\033[1;31m'
t = '\033[1;35m\'                                              \neeeee  eeeee e    e eeee eeeee       e  eeeee \n8   8  8   8 8    8 8    "   8       8  8   8 \n8eee8e 8eee8 8eeee8 8eee eeee8       8e 8e  8 \n88   8 88  8   88   88   88          88 88  8 \n88   8 88  8   88   88ee 88ee8       88 88ee8 \n                               eeeee\n\033[1;36m=============================================\n\033[1;32m ~ anthesphong1998@gmail.com (+6282195663814)\n\033[1;36m=============================================\n'
o = '\033[1;30m[\033[1;36m•\033[1;30m]'

api_id = 800812
api_hash = "db55ad67a98df35667ca788b97f771f5"

c = requests.Session()

def login():
  global data 
  os.system('clear')
  print(t)
  phone = input(f'{u}Input Your Number\t: {b}')
  if phone != '':
    with open('configuration.json','w') as fx:
      fx.write(json.dumps({"phone_number":phone}))
    print(f"{h}Sukses edit config !")
    time.sleep(1)
    main()
  else:
    print(f"{m}Edit config cancelled !")
    time.sleep(1)
    main()
    
def run():
  global data 
  os.system('clear')
  print(t)
  with open('configuration.json','r') as fo:
    json_val = fo.read()
    phone_number = json.loads(json_val)["phone_number"]
  if not os.path.exists("session"):
    os.makedirs("session")
  try:
    client = TelegramClient("session/" + phone_number, api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
      try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input('\033[1;35mEnter Your Code\t\t: \033[1;36m'))
      except SessionPasswordNeededError:
        passw = input("\033[1;35m2fa Password\t\t: \033[1;36m")
        me = client.sign_in(password=passw)
      print("\n=============================================\n")
      
    myself = client.get_me()
    peer = "@LtclaimBot"
    
    print (f'{u}Selamat datang di Bot {b}{peer}\n{u}Subscribe {b}youtube.com/c/RAYEZID\n')
    print (f'{b}='*45)

    client.send_message(client.get_entity(peer),message="Balance 💵")
    sleep(1)
    posts = client(GetHistoryRequest(client.get_entity(peer),limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    msg = posts.messages[0].message
    if 'Balance' in msg:
      inf = re.findall(':.+', msg)
      bal = inf[0]
      mem = inf[1]
      print (f"\n{u}Your Information:\n\n{o} {u}Your Name : {b}{myself.first_name}\n{o} {u}Your Balance {b}{bal}\n{o} {u}Your Refferall {b}{mem}\n\n=",f"{b}="*43)
      sleep(1)
      def task(cods):
        client.send_message(client.get_entity(peer),message=cods)
        sleep(2)
        posts_ = client(GetHistoryRequest(client.get_entity(peer),limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        msg_ = posts_.messages[0].message
        if 'getting' in msg_:
          link = re.findall('http.+', msg_)
          sf = link[0]
          su = link[1]
          r = requests.get('https://ipinfo.io/json')
          data = json.loads(r.text)
          print (f"\n{u}Your Task {cods}:\n\n{o} {u}Get Code Here : {b}{sf}\n{o} {u}Your Telegram ID {b}{myself.id}\n{o} {u}Your IP {b}{data['ip']}\n{o} {u}Submit Code Here {b}{su}\n\n=",f"{b}="*43)

      task("Code 1️⃣")
      input(f'{u} Press enter to continue ...\n')

      task("Code 2️⃣")
      input(f'{u} Press enter to continue ...\n')

      task("Code 3️⃣")
      input(f'{u} Press enter to exit ... ')

      exit('\n')

  except Exception as e:
    print(f"\n{m}Error, {e} !\n{m}System disconnect !")
    exit(f"{m}exit")
      
if __name__ == "__main__": 
  def main():
    os.system('clear')
    print(t)
    menu = input(f'{u}Selamat datang di Bot {b}@LtclaimBot\n{u}Subscribe {b}youtube.com/c/RAYEZID\n\n{b}1. Edit Config\n2. Run Bot\n\n{h}Masukkan Pilihan mu : ')
    if menu == '1':
      login()
    elif menu == '2':
      run()
    else:
      exit(f"{m}Exit")
  main()
