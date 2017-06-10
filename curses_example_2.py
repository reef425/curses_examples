'''
Created on Jun 7, 2017

@author: reef425@gamil.com
'''
import curses


urside=["Brown bear",
        "Polar bear",
        "Asian black bear",
        "American black bear",
        "Sun bear",
        "Sloth bear",
        "Spectacled bear",
        "Giant panda"]

bear=[
"    .--.              .--.",
"   : (\ \". _......_ .\" /) :",
"    '.    `        `    .'",
"     /\'   _        _   `\\",
"    /     0}      {0     \\",
"   |       /      \\       |",
"   |     /\'        `\\     |",
"    \\   | .  .==.  . |   /",
"     '._ \\.\' \\__/ \'./ _.\'",
"     /  ``'._-''-_.'``  \\"   ]


def myMenu(index=0):
    myScreen.erase()
    myScreen.addstr(1,5,"Menu:")
# Выводим на экран список медведей
    for i,item in enumerate(urside):
        if index!=i:
            myScreen.addstr(i+2,5, item)
        else:
# Строка на которой находится курсор будет выделенной с помощью атрибута curses.A_STANDOUT
            myScreen.addstr(i+2,5, item,curses.A_STANDOUT)
    myScreen.addstr(14,5,"Press \"enter\" get description")
    myScreen.addstr(15,5,"Press \"q\" for quit")
    myScreen.refresh()
    
def myDescription(index=0):
    myScreen.erase()
# Отображаем имя медведя из списка
    myScreen.addstr(1,5,"bear name: "+urside[index])
    myScreen.addstr(2,5,"description: ")
    for i,item in enumerate(bear):
        myScreen.addstr(i+3,5, item)
    myScreen.addstr(14,5,"Press \"up\",\"down\" back to menu")
    myScreen.addstr(15,5,"Press \"q\" for quit")
    myScreen.refresh()


def main():
    key = 'X'
    count=len(urside)-1
    index=0
# Включаем обработку дополнительных клавиш
    myScreen.keypad(True)
    myMenu()
    while key != ord('q'):
# Обработка curses.KEY_UP и curses.KEY_DOWN, нажатие вверх и вниз стрелок на клавиатуре
        key = myScreen.getch()
        if key==curses.KEY_UP:
            index-=1
            if index==-1:
                index=count
        if key==curses.KEY_DOWN:
            index+=1
            if index>count:
                index=0
# Обработка нажатия клавиши enter, curses.KEY_ENTER - обрабатывается не надежно поэтому добавляем
# дополнительную обратку key==10
        if key==curses.KEY_ENTER or key==10:
            myDescription(index)
        else:
            myMenu(index)
        myScreen.refresh() 


try:
    myScreen=curses.initscr()
# По умолчанию аргумент метода curses.curs_set() равен 1 - курсор отображается
# при curses.curs_set(0) курсор не отображется
    curses.curs_set(0)
    main()
finally:
    curses.endwin()

if __name__ == '__main__':
    pass