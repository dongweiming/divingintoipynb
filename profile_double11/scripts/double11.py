# coding=utf-8

import os
import sys
sys.path.append(os.path.expanduser('~/dev/shire'))
#import dongxi
from IPython.display import display
from IPython.html import widgets


def get():
    txt = widgets.TextWidget()
    display(txt)
    txt.value = 'Some Text'
