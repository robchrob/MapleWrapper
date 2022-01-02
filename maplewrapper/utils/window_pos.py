# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:28:33 2020

@author: Vincent Morel
"""

import win32gui

def process_coords(c_name):
    """
    Returns tuple (x0, y0, x1, y0) of process position on screen
    """
    hdl = win32gui.FindWindow(c_name, None)
    rect = win32gui.GetWindowRect(hdl)
    return rect

class_names = []
def callback(hwnd, extra):
    cname = win32gui.GetClassName(hwnd)
    class_names.append(cname)

def get_classname(search_term):
    win32gui.EnumWindows(callback, None)
    try:
        cname = [i for i in class_names if search_term in i]
        return cname[0]
    except IndexError:
        raise Invalid_Game_Window(f"Could not find the MapleStory process. Verify that the game is running. If it is running, modify the wrapper instantiation argument 'cname' to the corresponding process in the following list: {class_names}")

class Invalid_Game_Window(Exception):
    pass

if __name__ == '__main__':
    a = get_cname('MapleStory')
    print(process_coords(a))