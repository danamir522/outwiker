# -*- coding: utf-8 -*-

import wx

from outwiker.gui.preferences.baseprefpanel import BasePrefPanel

from .i18n import get_
from .prefpanelcontroller import PrefPanelController


class PreferencePanel(BasePrefPanel):
    """
    Панель с настройками
    """
    def __init__(self, parent, config):
        """
        parent - родитель панели(должен быть wx.Treebook)
        config - настройки из plugin._application.config
        """
        super(PreferencePanel, self).__init__(parent)

        global _
        _ = get_()

        self.__createGui()
        self.__controller = PrefPanelController(self, config)
        self.SetupScrolling()

    def __createGui(self):
        """
        Создать элементы управления
        """
        mainSizer = wx.FlexGridSizer(cols=1)
        mainSizer.AddGrowableCol(0)

        # Интервал обновлений
        intervalLabel = wx.StaticText(self, -1, _(u"Check for updates"))
        self.intervalComboBox = wx.ComboBox(
            self,
            -1,
            style=wx.CB_DROPDOWN | wx.CB_READONLY)

        self.intervalComboBox.SetMinSize((150, -1))

        intervalSizer = wx.FlexGridSizer(cols=2)
        intervalSizer.AddGrowableCol(0)
        intervalSizer.AddGrowableCol(1)

        intervalSizer.Add(intervalLabel,
                          1,
                          flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                          border=4)

        intervalSizer.Add(self.intervalComboBox,
                          1,
                          flag=wx.EXPAND | wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                          border=4)

        mainSizer.Add(intervalSizer, 1, flag=wx.EXPAND | wx.ALL, border=4)

        # Игнорировать нестибильные версии?
        self.ignoreUnstableCheckBox = wx.CheckBox(
            self,
            label=_(u"Ignore updates unstable versions"))

        mainSizer.Add(self.ignoreUnstableCheckBox,
                      flag=wx.ALIGN_CENTER_VERTICAL | wx.ALL,
                      border=4)

        self.SetSizer(mainSizer)
        self.Layout()

    def LoadState(self):
        self.__controller.loadState()

    def Save(self):
        self.__controller.save()
