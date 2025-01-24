# -*- coding: utf-8 -*-

import random
import curses

# 初始化屏幕
stdscr = curses.initscr()  # 修改: 修正变量名，使用stdscr而不是curses
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# 初始化蛇的位置和食物的位置
snk_x = sw//4
snk_y = sh//2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

# 游戏主循环
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # 计算蛇的新头部位置
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # 检查是否撞墙或撞自己
    if (new_head[0] in [0, sh] or 
        new_head[1] in [0, sw] or 
        new_head in snake[1:]):
        curses.endwin()
        quit()

    # 插入新头部
    snake.insert(0, new_head)

    # 检查是否吃到食物
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # 移除蛇的尾部
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # 绘制蛇的新头部
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)