# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class fsVOIManagerMain
###########################################################################

class fsVOIManagerMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Freesurfer VOI manager", pos = wx.DefaultPosition, size = wx.Size( 781,737 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer4defVOI = wx.StaticBoxSizer( wx.StaticBox( self.mainPanel, wx.ID_ANY, u"Extracted VOI list" ), wx.VERTICAL )
		
		defVOIListBoxChoices = []
		self.defVOIListBox = wx.ListBox( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, defVOIListBoxChoices, wx.LB_HSCROLL|wx.LB_MULTIPLE|wx.LB_NEEDED_SB )
		sbSizer4defVOI.Add( self.defVOIListBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.loadExtractedVOIFileButton = wx.Button( self.mainPanel, wx.ID_ANY, u"Load extracted VOI (.nii)", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4defVOI.Add( self.loadExtractedVOIFileButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.loadDefaultButton = wx.Button( self.mainPanel, wx.ID_ANY, u"Load default VOI list", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4defVOI.Add( self.loadDefaultButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( sbSizer4defVOI, 3, wx.EXPAND, 5 )
		
		bSizer4center = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4center.Add( self.m_panel2, 2, wx.EXPAND |wx.ALL, 5 )
		
		self.addButton = wx.Button( self.mainPanel, wx.ID_ANY, u"Add >>>", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer4center.Add( self.addButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.mergeButton = wx.Button( self.mainPanel, wx.ID_ANY, u"Merge as new >>>", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer4center.Add( self.mergeButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.merge2VOIButton = wx.Button( self.mainPanel, wx.ID_ANY, u"Merge to VOI >>>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4center.Add( self.merge2VOIButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer4center, 2, 0, 5 )
		
		bSizer4right = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4VOISetList = wx.StaticBoxSizer( wx.StaticBox( self.mainPanel, wx.ID_ANY, u"VOI set" ), wx.HORIZONTAL )
		
		list4VOISetChoices = []
		self.list4VOISet = wx.ListBox( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list4VOISetChoices, wx.LB_HSCROLL|wx.LB_NEEDED_SB|wx.LB_SINGLE )
		sbSizer4VOISetList.Add( self.list4VOISet, 5, wx.ALL|wx.EXPAND, 5 )
		
		bSizer4VOISetUpButton = wx.BoxSizer( wx.VERTICAL )
		
		self.openVOISetButton = wx.BitmapButton( self.mainPanel, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_TOOLBAR ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer4VOISetUpButton.Add( self.openVOISetButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.saveVOISetButton = wx.BitmapButton( self.mainPanel, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_TOOLBAR ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer4VOISetUpButton.Add( self.saveVOISetButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.renameVOIButton = wx.BitmapButton( self.mainPanel, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_HELP_SETTINGS, wx.ART_TOOLBAR ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer4VOISetUpButton.Add( self.renameVOIButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.removeVOIButton = wx.BitmapButton( self.mainPanel, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_CROSS_MARK, wx.ART_TOOLBAR ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer4VOISetUpButton.Add( self.removeVOIButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.upVOIButton = wx.BitmapButton( self.mainPanel, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_TOOLBAR ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer4VOISetUpButton.Add( self.upVOIButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.downVOIButton = wx.BitmapButton( self.mainPanel, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_TOOLBAR ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer4VOISetUpButton.Add( self.downVOIButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer4VOISetList.Add( bSizer4VOISetUpButton, 1, wx.ALIGN_TOP|wx.EXPAND, 5 )
		
		
		bSizer4right.Add( sbSizer4VOISetList, 6, wx.EXPAND, 5 )
		
		sbSizer4SelectedVOI = wx.StaticBoxSizer( wx.StaticBox( self.mainPanel, wx.ID_ANY, u"Contents for selected VOI" ), wx.VERTICAL )
		
		m_listBox4Choices = []
		self.m_listBox4 = wx.ListBox( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox4Choices, wx.LB_EXTENDED|wx.LB_HSCROLL|wx.LB_NEEDED_SB )
		sbSizer4SelectedVOI.Add( self.m_listBox4, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4right.Add( sbSizer4SelectedVOI, 4, wx.EXPAND, 5 )
		
		self.applyVOISetButton = wx.Button( self.mainPanel, wx.ID_ANY, u"Apply VOI set to NIfTI VOI file", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4right.Add( self.applyVOISetButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer4right, 4, wx.EXPAND, 5 )
		
		
		self.mainPanel.SetSizer( bSizer2 )
		self.mainPanel.Layout()
		bSizer2.Fit( self.mainPanel )
		bSizer1.Add( self.mainPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.loadExtractedVOIFileButton.Bind( wx.EVT_BUTTON, self.loadExtractedVOIFileButtonOnButtonClick )
		self.loadDefaultButton.Bind( wx.EVT_BUTTON, self.loadDefaultButtonOnButtonClick )
		self.addButton.Bind( wx.EVT_BUTTON, self.addButtonOnButtonClick )
		self.mergeButton.Bind( wx.EVT_BUTTON, self.mergeButtonOnButtonClick )
		self.merge2VOIButton.Bind( wx.EVT_BUTTON, self.merge2VOIButtonOnButtonClick )
		self.list4VOISet.Bind( wx.EVT_LISTBOX, self.list4VOISetOnListBox )
		self.openVOISetButton.Bind( wx.EVT_BUTTON, self.openVOISetButtonOnButtonClick )
		self.saveVOISetButton.Bind( wx.EVT_BUTTON, self.saveVOISetButtonOnButtonClick )
		self.renameVOIButton.Bind( wx.EVT_BUTTON, self.renameVOIButtonOnButtonClick )
		self.removeVOIButton.Bind( wx.EVT_BUTTON, self.removeVOIButtonOnButtonClick )
		self.upVOIButton.Bind( wx.EVT_BUTTON, self.upVOIButtonOnButtonClick )
		self.downVOIButton.Bind( wx.EVT_BUTTON, self.downVOIButtonOnButtonClick )
		self.applyVOISetButton.Bind( wx.EVT_BUTTON, self.applyVOISetButtonOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def loadExtractedVOIFileButtonOnButtonClick( self, event ):
		event.Skip()
	
	def loadDefaultButtonOnButtonClick( self, event ):
		event.Skip()
	
	def addButtonOnButtonClick( self, event ):
		event.Skip()
	
	def mergeButtonOnButtonClick( self, event ):
		event.Skip()
	
	def merge2VOIButtonOnButtonClick( self, event ):
		event.Skip()
	
	def list4VOISetOnListBox( self, event ):
		event.Skip()
	
	def openVOISetButtonOnButtonClick( self, event ):
		event.Skip()
	
	def saveVOISetButtonOnButtonClick( self, event ):
		event.Skip()
	
	def renameVOIButtonOnButtonClick( self, event ):
		event.Skip()
	
	def removeVOIButtonOnButtonClick( self, event ):
		event.Skip()
	
	def upVOIButtonOnButtonClick( self, event ):
		event.Skip()
	
	def downVOIButtonOnButtonClick( self, event ):
		event.Skip()
	
	def applyVOISetButtonOnButtonClick( self, event ):
		event.Skip()
	

