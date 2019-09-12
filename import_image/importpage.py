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

class ImportImageCtrl(scrolledpanel.ScrolledPanel):
    pageName = "ImportPage"
    def __init__(self, parent, style=wx.TAB_TRAVERSAL):
        super(ImportImageCtrl, self).__init__(parent, style=style)
        
        # Layout
        self.__DoLayout()
        self.SetInitialSize()


    def __DoLayout(self):

        title_lbl= wx.StaticText(self, label="Import Image")
        font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        title_lbl.SetFont(font)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(title_lbl, 0, wx.ALL, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)

        sizer = wx.GridBagSizer(vgap=2, hgap=2)
        nameLbl = wx.StaticText(self, -1, "Name:")

        nameStr = 'Prelimary Assessment'
        self.name = wx.StaticText(self, -1, nameStr)

        sizer.Add(nameLbl, (1, 1))
        sizer.Add(self.name, (1, 2))

        discriptionLbl = wx.StaticText(self, -1, "Discription:")
        
        discriptionStr = 'Inital assessment of the patent'
        self.discription = wx.StaticText(self, -1, discriptionStr)

        sizer.Add(discriptionLbl, (2, 1))
        sizer.Add(self.discription, (2, 2))
        
        amountLbl = wx.StaticText(self, -1, "Amount:")
        amountStr = '38.50'
        sizer.Add(amountLbl, (5, 1))
        self.amount = wx.StaticText(self, -1, amountStr)
        sizer.Add(self.amount, (5, 2))
        



        btnszr = wx.StdDialogButtonSizer()
        editbtn = wx.Button(self, wx.ID_EDIT)
        openbtn = wx.Button(self, wx.ID_OPEN)
        editbtn.SetDefault()
        sizer.Add(editbtn, (8, 3))
        sizer.Add(openbtn, (8, 4))

        btnszr.Realize()

        #listSizer = wx.GridBagSizer(vgap=2, hgap=2)
        #listSizer.Add(self.backupsListCtrl, (1, 1))
        mainSizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 10)
        #mainSizer.Add(btnszr, 0, wx.ALIGN_LEFT, 12)
        #mainSizer.Add(listSizer, 0, wx.EXPAND | wx.ALL, 10)

        self.SetSizer(mainSizer)



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

        self.importImageCtrl = ImportImageCtrl(self)
        self.AddPage(self.importImageCtrl, "Import Images")


class TestApp(wx.App):
    
    def OnInit(self):
        frame = MainFrame(None, title="The Main Frame")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__=="__main__":

    app = TestApp(False)
    app.MainLoop()
