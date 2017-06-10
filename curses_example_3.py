'''
Created on Jun 6, 2017

@author: reef425@gamil.com
'''
import curses

textAttributes=["A_BLINK",
    "A_BOLD",
    "A_DIM",
    "A_REVERSE",
    "A_STANDOUT",
    "A_UNDERLINE"]

# Спиок атрибутов для выделения строки
attributes=[curses.A_BLINK,
    curses.A_BOLD,
    curses.A_DIM,
    curses.A_REVERSE,
    curses.A_STANDOUT,
    curses.A_UNDERLINE,]



def myMenu(index=0):
    if index>6:
        index=0
    myScreen.erase()
    myScreen.addstr(1,5, "Text:")
    myScreen.addstr(2,5, "The spectacle before us was indeed sublime ",attributes[index])
    myScreen.addstr(3,5, "Select text Attribute:")
# Отображение списка атрибутов
    for i,item in enumerate(textAttributes):
            myScreen.addstr(i+4,5, item+"  enter key: "+str(i+1))
    myScreen.addstr(10,5, "Press key:")
    myScreen.addstr(12,5, "Press \"q\" for quit")
    myScreen.addstr(13,5, "Press \"l\" get loop menu")
    myScreen.refresh()

def main():
    key = 'X'
    index=0
    while key != ord('q'):
        myMenu(index)
# Устанавливаем курсор в точку (10,16)
        key = myScreen.getch(10,16)
# Добавляем в строку символ котоый получили при нажатии, в качестве аргумента
# передается код в ASCII таблице
        myScreen.addch(10,16,key)
        for item in range(1,7):
            if key==ord(str(item)):
                index=item-1
        if key == ord('l'):
            subScreen()
        myScreen.refresh() 


def subScreen():
# При myScreen.nodelay(1) включаем не блокируемый режим ввода  (по умолчанию myScreen.nodelay(0)).
# В этом режиме myScreen.getch() возвращает -1
# Если этого не сделать цикл оставновится и будет ждать ввода пользователя.
    myScreen.nodelay(1)
    curses.curs_set(0)
    anm = [" / ", "---", " \\ ", " | "]
    key = 'X'
    i=0
    while key != ord('m'):
        myScreen.erase()
        myScreen.addstr(5, 5, anm[i])
# Метод curses.napms(500) аналогичен time.sleep(0.5), программа засыпает на 500 милисекунд
        curses.napms(500)
        i+=1
        if i==4:i=0
        myScreen.addstr(13, 5, "Press \"m\" get main menu")
        myScreen.refresh()
        key = myScreen.getch()
    myScreen.nodelay(0)
    curses.curs_set(1)

try:
    myScreen=curses.initscr()
    main()
finally:
    curses.endwin()

if __name__ == '__main__':
    pass