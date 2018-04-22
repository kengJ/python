import os
import time

#https://www.jianshu.com/p/10e347c4bd78
#https://blog.csdn.net/zhangpfly/article/details/78230625?locationNum=9&fps=1

'''
ps -ef|grep wx.py|grep -v grep > wx.lock
grep -v <匹配字段> 排除匹配字段之外的
ps -ef 查询进程
grep <进程关键字> 根据关键字查询
>filename 是把结果输出到什么文件
程序只要检查指定文件里是否有内容，即可得出程序是否被运行
'''

'''
linux 定时任务实现
crontab 命令
–e : 修改 crontab 文件. 如果文件不存在会自动创建
–l : 显示 crontab 文件
-r : 删除 crontab 文件
-ir : 删除 crontab 文件前提醒用户

格式:{minute} {hour} {day-of-month} {month} {day-of-week} {full-path-to-shell-script} 

例子:
1. 在 12:01 a.m 运行，即每天凌晨过一分钟。这是一个恰当的进行备份的时间，因为此时系统负载不大。
    1 0 * * * /root/bin/backup.sh
2. 每个工作日(Mon – Fri) 11:59 p.m 都进行备份作业。
    59 11 * * 1,2,3,4,5 /root/bin/backup.sh
    下面例子与上面的例子效果一样：
    59 11 * * 1-5 /root/bin/backup.sh
3. 每5分钟运行一次命令
    */5 * * * * /root/bin/check-status.sh
4. 每个月的第一天 1:10 p.m 运行
    10 13 1 * * /root/bin/full-backup.sh
5. 每个工作日 11 p.m 运行。
    0 23 * * 1-5 /root/bin/incremental-backup.sh
'''
def cmd():
    process = '/home/keng/test.lock'
    cmd = 'ps -ef | grep wx.py|grep -v grep >%s' % process
    os.system(cmd)
    #os.path.getsize(cmd)
    if not os.path.getsize(process):
        os.system("nohup /home/pi/wx.py &")

def callmail():
     msg = MIMEMultipart('related') 
     msg['from'] = '110@163.com' 
     msg['to'] = '110@163.com' 
     msg['subject'] = 'Robot Dead**'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) 
     content = "Your Robot Dead" 
     txt=MIMEText(content) 
     msg.attach(txt) 
     smtp=smtplib 
     smtp=smtplib.SMTP() 
     smtp.connect('smtp.163.com','25') 
     smtp.login('110@163.com','xxxxxxx') 
     smtp.sendmail('110@163.com','110@163.com',msg.as_string()) 
     smtp.quit()

def main():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    print(now)

if __name__ in '__main__':
    main()