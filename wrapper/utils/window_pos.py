# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:28:33 2020

@author: Vincent Morel
"""

import win32gui

def process_coords(p_name):
    """
    Returns tuple (x0, y0, x1, y0) of process position on screen
    """
    hdl = win32gui.FindWindow(None, p_name)
    rect = win32gui.GetWindowRect(hdl)
    return rect

# def callback(hwnd, extra):
#     rect = win32gui.GetWindowRect(hwnd)
#     x = rect[0]
#     y = rect[1]
#     w = rect[2] - x
#     h = rect[3] - y
#     print("Window %s:" % win32gui.GetWindowText(hwnd))
#     print("\tLocation: (%d, %d)" % (x, y))
#     print("\t    Size: (%d, %d)" % (w, h))

# def main():
#     win32gui.EnumWindows(callback, None)
 

if __name__ == '__main__':
    print(process_coords("MapleStory"))
    # main()