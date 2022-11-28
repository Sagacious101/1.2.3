from createhero import *
import os


os.system("cls")
p1 = make_hero(money=100, mp_curret=19, mage=True)
buy_item(p1, "зелье маны", 10)
show_hero(p1)
consume_item(p1, 0)
show_hero(p1)

