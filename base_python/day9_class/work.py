# -*- conding:utf-8 -*-
# 编写“计算机类”，属性包括CPU型号，内存大小，硬盘大小。
# 行为包括介绍CPU型号，展示内存大小，展示硬盘大小，综合介绍。
class Computer:
      def __init__(self,CPU,internal_storage,hard_disk):
            self.CPU=CPU
            self.internal_storage=internal_storage
            self.hard_disk=hard_disk
      def infor_CPU(self):
            return self.CPU
      def infor_storage(self):
            return self.internal_storage
      def infor_disk(self):
            return self.hard_disk
      def infor_all(self):
            return f'CPU 的规格{self.CPU},内存条大小{self.internal_storage},硬盘的规格{self.hard_disk}'
c=Computer('i7','3G','6G')
print(c.infor_CPU())
print(c.infor_storage())
print(c.infor_disk())
print(c.infor_all())

# 编写一个银行卡类，具有账号，人名与余额属性。编写提款机类，接收一张银行卡，并且具有存款，提款，查询余额，转账功能。
class BankCard:
      def __init__(self,id,name,money):
            self.id=id
            self.name=name
            self.money=money
class ATM:
      def __init__(self,name):
            self.name=name
      def in_money(self,bankCard,number):
            bankCard.money +=number
      def out_money(self,bankCard,number):
            bankCard.money -=number
      def search_infor(self,bankCard):
            print(bankCard.money)
      def trans_money(self,bankCard,card2,number):
            self.out_money(bankCard,number)
            self.in_money(bankCard2,number)
bankCard=BankCard('001','lz',9999)
bankCard2=BankCard('002','lzz',100)
atm=ATM('工行')
atm.trans_money(bankCard,bankCard2,100)
atm.search_infor(bankCard)
atm.search_infor(bankCard2)

# 编写一个计数器，能够记录一个类创建了多少个对象。

class Counter:
      num=0
      def __init__(self):
            pass
      @classmethod
      def count(cls):
            cls.num += 1
      @classmethod
      def totall(cls):
            print(cls.num)
class TestC:
      def __init__(self,counter):
            self.counter=counter
            counter.count()
counter=Counter()
for i in range(5):
      TestC(counter)
counter.totall()
# 将第一题中的计算机对象放入列表中输出，会出现什么现象？
li=[Computer('i3',3,4),Computer('i5',6,7),Computer('i7',8,8)]
print(li)
# 编写程序，设计单张扑克牌类Card，具有花色，牌面与具体值。
# 同时设计整副扑克牌类Cards，具有52张牌。Cards类能够具有发牌，对任意三张牌断定牌的类型。
import random
class Card:
      colors=['红砖','黑桃','梅花','红桃']
      faces=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
      values=[1,2,3,4,5,6,7,8,9,10,11,12,13]
      def __init__(self,color,face,value):
            self.color=color
            self.face=face
            self.value=value
      def infor(self):
            print(f'花色：{self.color}，牌面：{self.face}，数值：{self.value}')
class Cards:
      cards=[]
      def __init__(self):
            pass

      def del_cards(self):
            li=[]
            for i in range(3):
                  index=random.randint(0,51)
                  li.append(self.__class__.cards[index])
            return li
      def judge(self,li):
             worth=[li[0].value,li[1].value,li[2].value]
             big=max(worth)
             small=min(worth)
             if li[0].value==li[1].value==li[2].value:
                  return '豹子！'
             if li[0].value==li[1].value or li[0].value==li[2].value or li[2].value==li[1].value:
                  return '对子！'
             if li[0].color==li[1].color==li[2].color:
                   if big- small==2:
                         return '同花顺'
                   return '同花'
             if big-small==2:
                   return '顺子！'
             else:
                   return '散牌！'
      def new_cards(self,Card):
            for c in Card.colors:
                  for f,v in enumerate(Card.faces,1):
                        self.__class__.cards.append(Card(c,v,f))

cards=Cards()
cards.new_cards(Card)
li=cards.del_cards()
print(cards.judge(li))
for i in li:
      i.infor()



