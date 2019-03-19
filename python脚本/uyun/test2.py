#coding:utf-8
#!/usr/bin/env python
import wx
app = wx.App()
win = wx.Frame(None,-1,'install test')
btn = wx.Button(win, label = 'Button')
win.Show()
app.MainLoop()