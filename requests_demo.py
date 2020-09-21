# -*- coding: UTF-8 -*=

x=28.5
m=5    #杠杆配置倍数
a=4.11365956 #交易币余额数量
b=23.44226580	#计价币余额
c=0 #已借交易币数量
d=112.000001	#已借计价币数量
e_hour=1 	#已借交易币小时
f_hour=1	#已借计价币小时
e=c*0.000021*e_hour	#交易币利息
f=d*0.000021*f_hour  #计价币利息
rank=1.0011 #爆仓设置的风险率


#总资产
summary=a*x+b
print("总资产等于%s"%summary)
#未还借入资产
borrow=c*x+d
print("未还借入资产等于%s"%borrow)
#未还利息
interest=e*x+f
print("未还利息%s"%interest)



print("交易币利息%s"%round(e,9))
print("计价币利息%s"%f)
#可借最大计价币
max_borrow=(summary-borrow-interest)*(m-1)-borrow
print("可借最大计价币%s"%round(max_borrow,5))

#可借最大交易币
max_trad=max_borrow/x
print("可借最大交易币保留6位截取%s "%round(max_trad,9))

#风险率
risk=(summary-interest)/borrow
res = format(risk, '.4%')
print("风险率保留两位%s"%res)
if risk>3:
	print("无风险")
else:
	print("有风险")

#爆仓价
baocang=(rank*d+f-b)/(a-e-rank*c)
print("爆仓价%s"%str(baocang))


#最大可转出的计价币
roll_borrow=(summary-interest)-borrow*(m/(m-1))
print("最大可转出的计价币%s"%str(roll_borrow))

#最大可转出的交易币
roll_trad=roll_borrow/x
print("最大可转出的交易币%s" %str(roll_trad))


#破产价格
bankruptcy_price=(d+f-b)/(a-e-c)
print("破产价格为%s"%bankruptcy_price)

# 账户内交易币总数*X+账户内计价币总数-未还交易币利息个数*X-未还计价币利息个数 =未还交易币个数*X+未还计价币个数
# 账户内交易币总数-未还交易币利息个数-未还交易币个数=未还计价币个数+未还计价币利息个数-账户内计价币总数
# a-e-c=(d+f-b)/(a-e-c)