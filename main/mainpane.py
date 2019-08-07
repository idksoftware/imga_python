'''
Created on Jul 11, 2013

@author: wzw7yn
'''
import wx

from import_image.importpage import ImportImageCtrl
from export_image.exportpage import ExportImageCtrl
from checkin_image.checkinpage import CheckinImageCtrl
from checkout_image.checkoutpage import CheckoutImageCtrl
#from gps.gpspage import GPCtrl
#from appointment.appointmentspage import AppointmentsCtrl
#from exportpage import EquipmentCtrl
#from patent.currentpatentpage import CurrentPatentCtrl
#from import.importpage import FinanceCtrl
#from treatment.treatmentpage import TreatmentsCtrl
#from cpd.cpdpage import CPDCtrl

class MainPane(wx.Notebook):

    def __init__(self, parent):
        super(MainPane, self).__init__(parent, style=wx.NB_TOP)


        self.importImageCtrl = ImportImageCtrl(self)
        self.exportImageCtrl = ExportImageCtrl(self)
        self.checkinImageCtrl = CheckinImageCtrl(self)
        self.checkoutImageCtrl = CheckoutImageCtrl(self)
        
        self.AddPage(self.importImageCtrl, "Import")
        self.AddPage(self.exportImageCtrl, "Export")
        self.AddPage(self.checkinImageCtrl, "Check-in")
        self.AddPage(self.checkoutImageCtrl, "Check-out")
        
