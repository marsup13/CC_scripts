#SCENARIO 1: SQLITE DB, USING VM2, IP=http://20.127.1.102/

import requests,re,random,threading,string,re
# re: regular expression


def register():
  global a
  try:
    ses=requests.session()
    #The Session object allows you to persist certain parameters across requests. 
    #It also persists cookies across all requests made from the Session instance, 
    #and will use urllib3’s connection pooling. 
    req=ses.get("http://20.127.1.102/register",timeout=20)
    a+=1
    ree=re.findall('<input id="csrf_token" name="csrf_token" type="hidden" value="(.*?)">',req.text)
    raa=''.join(random.choice(string.ascii_lowercase) for i in range(5))
    formData = {
    "csrf_token": ree[0],
    "email": raa+"@gmail.com",
    "name": raa,
    "next": "",
    "password": "azerty123",
    "password_confirm": "azerty123",
    "submit": "Register",
    "username": raa+"65"
    }
    print(ses.post("http://20.127.1.102/register",data=formData,timeout=20).status_code)
    a+=1
  except:
    print("erreur")
    pass


def add_post():
    global a
    ses=requests.session()
    req=ses.get("http://20.127.1.102/",timeout=20)
    a+=1
    ree=re.findall('<input id="csrf_token" name="csrf_token" type="hidden" value="(.*?)">',req.text)
    data={"title":'sqlite',"description":'sqlite DB version using only one VM',"csrf_token":ree[0]}
    print(ses.post("http://20.127.1.102/",data=data,timeout=20).status_code)
    a+=1

print('Starting scenario1 SQLITE...')
a=0
threadnum = 10
threads = []
for i in range(1500): # N requests in total that will be splitted into threads of 10 each one
  thread = threading.Thread(target=random.choice([register,add_post]))
  threads.append(thread)
  thread.start()
  if len(threads) == threadnum:
    for threadd in threads:
      threadd.join()
      print("thread completed successfully!")
    threads = []
print("nb requests:",a)
print('Scenario1 SQLITE FINISHED!...')