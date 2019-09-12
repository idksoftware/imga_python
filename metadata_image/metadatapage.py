'''
Created on Jan 7, 2014

@author: wzw7yn
'''
import wx
import os

from datetime import datetime
from datetime import timedelta

#from patenteditdlg import PatentEditDialog

import wx.lib.scrolledpanel as scrolledpanel
#from access.patent import PatentTable

class MetedataCtrl(scrolledpanel.ScrolledPanel):
    pageName = "Metadata Page"
    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(MetedataCtrl, self).__init__(parent, style=style)
        

        #patentTable = PatentTable()
        #self.rows = patentTable.showAll()
        #self.backupsListCtrl.populateList(self.rows)
        # Layout
        self.__DoLayout()
        self.SetInitialSize()


    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Apply metadata to Images")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)





    '''    
        self.SetSizer(mainSizer)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClicked)

    def OnClicked(self, event):
        self.selected_row = event.GetIndex()
        ##self.rows[self.selected_row]
        from paymentdlg import PaymentEditDialog
        paymentEditDialog = PaymentEditDialog()
        paymentEditDialog.ShowModal()

    def OnItemSelected(self, event):
        self.selected_row = event.GetIndex()
    '''


class MainFrame(wx.Frame):
    
    def __init__(self, parent, id=wx.ID_ANY, title="",pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, name ="myFrame"):
        super(MainFrame, self).__init__(parent, id, title, pos, size, style, name)

        self.panel = MainPane(self)
    
class MainPane(wx.Notebook):

    def __init__(self, parent):
        super(MainPane, self).__init__(parent, style=wx.NB_LEFT)

        self.checkinImageCtrl = MetedataCtrl(self)
        self.AddPage(self.MetedataCtrl, "Apply metadata to Images")


class TestApp(wx.App):
    
    def OnInit(self):
        frame = MainFrame(None, title="The Main Frame")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
