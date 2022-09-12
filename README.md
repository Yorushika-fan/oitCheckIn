# 🌈oitCheckIn

## ✨项目介绍

​	由于疫情原因，自从20年来到学校已经打卡将近两年左右，此期间也有忘记打卡或者打卡时间太迟被老师催促。项目是为了帮助大家定时打卡，如果出现不良症状及时上报学校。疫情防控，人人有责。

## 🔰项目功能

-  学号加身份证后6位填报体温
-  自动获取上次打卡信息提交打卡数据
-  支持多人打卡
-  支持server酱微信推送

## 💃支持学校

**（默认oit）在post.py中替换你的学校**

  - 包头师范学院:bttc
  - 东北财经大学：dufe
  - 集宁师范学院：jntc
  - 内蒙古医科大学:immu
  - 内蒙古民族大学:imun
  - 乌兰察布职业学院：wlcbzyxy
  - 鄂尔多斯职业学院：ordosvc
  - 包头钢铁职业技术学院：btsvc
  - 辽宁广播电视大学:lntvu
  - 鄂尔多斯应用技术学院:oit



## 🎨配置文件

- config.json中配置

- **username**为学号(**必填**)

- **password**为身份证后6位(**必填**)

- **key**：server酱微信推送密钥(**必填**)（tips：打卡成功后微信推送消息）
  
  - 推送能每天看到是否填报成功
  - [点击打开server酱官网](https://sct.ftqq.com/sendkey)
  - 微信登陆，点击上方sendkey，复制你的sendkey
  
- @name:备注（可以为空）

- 例子:支持多人

  ```json
  [
      
     
  
  
           {
                  "username": "202071xx",
                  "password": "26xx",
                  "key": "SCT18713TIMYxxx",
                  "@name": "xx"
          },
  
  
          {
                  "username": "202071xxx",
                  "password": "220xx",
                  "key": "SCT8131xx",
                  "@name": "大xxx"
          },
          {
                  "username": "2020xxxx",
                  "password": "042xxx",
                  "key": "SCT147448T7atGxxxxx",
                  "@name": "成功xx"
           },
  
          {
                  "username":"20191xxx",
                  "password":"14xxxx",
                  "key":"SCT168556Txxxxx",
                  "@name":"xx"
  
  
          }
  
  
  
  
  
  ]
  
  ```

  

## 💦使用方法（服务器）

- 克隆项目，编辑配置文件

```shell
git clone https://github.com/Clost-java/oitCheckIn.git
cd oitCheckIn
vi config.json
pip3 install -r requirements.txt
```

- 设置定时运行 (路径根据自己实际情况)

```shell
crontab -e
0 6 * * * cd /home/checkIn/oitCheckIn/ ; python3 main.py >> log.txt

```

## 🙋‍出现问题

业余python，如果出现不能使用的可以及时反馈

​	[联系我](https://qm.qq.com/cgi-bin/qm/qr?k=CkxZdTs29r2FkJ37H02MCx1sKpNFRpUL&noverify=0)

























