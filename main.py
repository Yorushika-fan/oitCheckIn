#coding=utf-8
import json
from time import time
from user import User
from post import UserApi
import time

def main():
  
   
    with open("config.json", 'r', encoding='utf8') as St:
        json_data = json.load(St)
  
    for x in range(0,len(json_data)):
        username = json_data[x]["username"]
        password = json_data[x]["password"]
        key = json_data[x]["key"]
        userAPI = UserApi(User(username,password,key))
        cookie = userAPI.login()
        userAPI.report(cookie)
        time.sleep(10)
        userAPI.push()
    
if __name__ == '__main__':
    main()
    
