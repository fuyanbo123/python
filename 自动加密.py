import easygui as eg
import time

before_password = eg.enterbox("请输入你需要加密的密码：", "自动加密")
protect_numbers = int(eg.enterbox("请输入一个保密数字：", "自动加密"))

after_password = []
eg.msgbox("是否加密？")
time.sleep(1)
for i in before_password:	
	after_password.append(chr(ord(i) + protect_numbers))
	
look = ''.join(after_password)




eg.enterbox("加密后的密码是：", "自动加密", look)

eg.msgbox("感谢你使用我们的加密小程序！！！")