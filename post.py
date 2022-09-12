# -*- coding: utf8 -*-
import json
import datetime
import requests
import random
from user import User
mysession = requests.session()
class UserApi:
    def __init__(self, user: User) -> None:
        self.user = user
        userAgents = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
        ]
        self.userAgent = random.choice(userAgents)
        
    
    #登录
    def login(self):
        url = "http://open.smilecampus.cn/app.php/epidemic_survey/index/login"
        headers = {
            "user-agent":self.userAgent
        }
        data = {
        "user_code": self.user.username,  # 学号
        "school": "oit",
        "id_code": self.user.password  # 身份证后6位
                }
        res=requests.post(url=url, data=data,headers=headers)
        return res.cookies

    #填报
    def report(self,cookie):
        #填报链接
        url = 'http://open.smilecampus.cn/app.php/epidemic_survey/index/report_by_day'

        #获取历史记录链接
        url2 = 'https://open.smilecampus.cn/app.php/epidemic_survey/index/get_report_list_by_day'

        headers = {
            "user-agent":self.userAgent
        }
        
        #获取前一天的体温填报信息进行填报
        info = json.loads(requests.get(url2,cookies=cookie).text)
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        userAddress = (info["data"][yesterday]["address"]["address"])



        address = {
        "address": info["data"][yesterday]["address"]["address"],
        "recommend": info["data"][yesterday]["address"]["recommend"],
        "nation": "中国",
        "province": "中国",
        "city": "中国",
        "district": "中国",
        "street": "中国"
       
        
            }
        data = {
	    "temperature": "正常",
	    # "symptom": "",
	    "mental_status": "平静",
	    "mental_symptom": "",
	    "latitude": info["data"][yesterday]["latitude"],
	    "longitude": info["data"][yesterday]["longitude"],
        "address":json.dumps(address),
        "home_quarantine": "0",
        "cohabitant_symptom": "0",
        "confirm_commitment": "1",
        "is_cough": "0",
        "is_weak": "0",
	"cohabitant_danger_zone":"0",
        "is_chest_tight": "0",
        "extra":"null",
        "home_address": info["data"][yesterday]["home_address"],
        "home_address_detail": info["data"][yesterday]["home_address_detail"]
            
            }
       #post填报
        res = requests.post(url,headers=headers,data=data,cookies=cookie).text
        print(res)


        self.detail = res
        if "感谢填报" in res :
            self.info =  userAddress + "填报成功"
        else:
            self.info  =  "填报失败"


         
        
    #推送 
    def push(self):
        url = 'https://sctapi.ftqq.com/'+self.user.key+'.send'
        
        data = {
            "title":self.info,
            "desp":self.detail
        }
        print( datetime.date.today().strftime('%y-%m-%d') + "\t\t" + self.user.username + "\n" + self.info)
        
        
        requests.post(url,data=data)
        
        
        
        

        



   
    



