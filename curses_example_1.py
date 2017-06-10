'''
Created on Jun 6, 2017

@author: reef425@gamil.com
'''
import curses


def main():
    key = 'X'
#Очищаем экран.
    myScreen.erase()
#Добавляем строку начиная с точки (2,5) и (5,5).
    myScreen.addstr(2, 5, "Press any key:")
    myScreen.addstr(5, 5, "Press \"q\" for quit")
#Начинается цикл, выход из цикла при нажатии кнопки q на клавиатуре
# ord("q") возвращает код в ASCII таблице, chr(10) по код возвращет симвод из таблицы.
    while key != ord('q'):
# myScreen.getch(2,20) устанавливаем курсор в точку (2,20) и возвращаем код символа, если точка не задана
#  то курсор устанавливется в конец последней строки.
# myScreen.getkey(2,20) возвращаем символ
# myScreen.getstr(2,20) возвращаем всю строку
        key = myScreen.getch(2,20)
        myScreen.erase()
        myScreen.addstr(2, 5, "Press any key:")
        myScreen.addstr(5, 5, "Press \"q\" for quit")
        myScreen.addstr(3, 5, "Key:" + (chr(key) + " des:" + str(key)))
#Обновление.
        myScreen.refresh()

try:
#Инициализация screen.
    myScreen = curses.initscr()
    main()

finally:
# Инициализация конца работы программы, обязательно.
    curses.endwin()

if __name__ == '__main__':
    pass