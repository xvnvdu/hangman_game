import time
import sys

def loading_bar():
    timer = 1.8
    loading = '_'
    loading_2 = ''
    space = ' '
    space_count = 17
    space_count_2 = 18
    percent = 5
    while timer > 0.95:
        print(f'\r|{loading}{space * space_count}{round(percent, 1)}%{space * space_count_2}|', end='')
        sys.stdout.flush()
        time.sleep(0.07)
        loading += '_'
        space_count -= 1
        timer -= 0.05
        percent += 2.71
    while 0 < timer < 0.95:
        print(f'\r|{loading}{space * space_count}{round(percent, 1)}%{loading_2}{space * space_count_2}|', end='')
        sys.stdout.flush()
        time.sleep(0.07)
        loading_2 += '_'
        space_count_2 -= 1
        timer -= 0.05
        percent += 2.72
    time.sleep(0.5)