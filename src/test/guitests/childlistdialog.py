#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

from basemainwnd import BaseMainWndTest
from outwiker.pages.wiki.actions.childlist import ChildListDialog, ChildListDialogController
from outwiker.core.application import Application


class ChildListDialogTest (BaseMainWndTest):
    """
    Тесты окна со списком прикрепленных файлов
    """
    def setUp (self):
        BaseMainWndTest.setUp (self)
        self._dialog = ChildListDialog (Application.mainWindow)


    def testCancel (self):
        controller = ChildListDialogController (self._dialog)
        self._dialog.SetModalResult (wx.ID_CANCEL)
        result = controller.getDialogResult()

        self.assertEqual (result, None)


    def testSortByOrder (self):
        controller = ChildListDialogController (self._dialog)
        
        self._dialog.SetModalResult (wx.ID_OK)
        self._dialog.selectedSort = 0
        self._dialog.isDescend = False

        result = controller.getDialogResult()

        self.assertEqual (result, u"(:childlist:)")


    def testSortByOrderDescend (self):
        controller = ChildListDialogController (self._dialog)
        
        self._dialog.SetModalResult (wx.ID_OK)
        self._dialog.selectedSort = 0
        self._dialog.isDescend = True

        result = controller.getDialogResult()

        self.assertEqual (result, u"(:childlist sort=descendorder:)")


    def testSortByName (self):
        controller = ChildListDialogController (self._dialog)
        
        self._dialog.SetModalResult (wx.ID_OK)
        self._dialog.selectedSort = 1
        self._dialog.isDescend = False

        result = controller.getDialogResult()

        self.assertEqual (result, u"(:childlist sort=name:)")


    def testSortByNameDescend (self):
        controller = ChildListDialogController (self._dialog)
        
        self._dialog.SetModalResult (wx.ID_OK)
        self._dialog.selectedSort = 1
        self._dialog.isDescend = True

        result = controller.getDialogResult()

        self.assertEqual (result, u"(:childlist sort=descendname:)")