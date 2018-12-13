# -*- coding:utf-8 -*-
# @Author  : LZ
# @Time    : 2018/4/13 18:38
import threading
# 当创建一个线程时，该线程是前台线程还是后台线程？
#strat启动后变成前台程序，执行完毕销毁后变成后天程序
# 编写两个线程，对同一个全局变量增加若干次（次数多一点），会出现什么情况。
num = 0
def f_mult():
    global num
    for i in range(1000000):
        num += 1
# t1 = threading.Thread(target=f_mult)
# t2 = threading.Thread(target=f_mult)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(num)

# 两个线程，使用同一个函数作为target，然后在函数定义一个局部变量，两个线程分别对该变量自增若干次，会出现什么情况。
def f_2():
    n = 0
    for i in range(10000000):
        n += 1
    print(n)
# t1 = threading.Thread(target=f_2)
# t2 = threading.Thread(target=f_2)
# t1.start()
# t2.start()

# 编写买家与卖家交易的程序，一个钱锁，一个货锁，并造成死锁。
class Goods():
    """
    商品类
    """
    def __init__(self,name,num,price):
        self.name = name
        self.num = num
        self.price = price
class Seller():
    def __init__(self,goods,g_lock):
        self.goods = goods
        self.g_lock = g_lock
    def seller_good(self,n,buyer):
        g_lock.acquire()
        buyer.m_lock.acquire()
        self.goods.num -= n
        buyer.money -= self.goods.price * n
        g_lock.release()
        buyer.m_lock.release()
    def __call__(self, *args, **kwargs):
        print(self.goods.name,self.goods.num)
class Buyer():
    def __init__(self,money,m_lock):
        #threading.Thread.__init__(self)
        self.money = money
        self.m_lock = m_lock
    def buy_goods(self,n,seller):
        self.m_lock.acquire()
        seller.g_lock.acquire()
        seller.goods.num -= n
        self.money -= seller.goods.price * n
        seller.g_lock.release()
        self.m_lock.release()
    def __call__(self, *args, **kwargs):
        print(self.money)

g_lock = threading.RLock()
m_lock = threading.RLock()
goods = Goods('Wake me up at nine thirty',10,100)
seller =Seller(goods,g_lock)
buyer = Buyer(1000,m_lock)
s = threading.Thread(target=seller.seller_good,args=(6,buyer))
b = threading.Thread(target=buyer.buy_goods,args=(6,seller))
s.start()
#b.start()
#s.join()
#b.join()
print(seller.goods.num)
print(buyer.money)