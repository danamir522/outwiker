# -*- coding: UTF-8 -*-

import os.path

from outwiker.core.pluginbase import Plugin
from outwiker.core.commands import getCurrentVersion
from outwiker.core.version import Version, StatusSet

from .stylecommand import StyleCommand

__version__ = u"2.0"


if getCurrentVersion() < Version(2, 1, 0, 833, status=StatusSet.DEV):
    print ("Style plugin. OutWiker version requirement: 2.1.0.833")
else:
    class PluginStyle (Plugin):
        """
        Плагин, добавляющий обработку команды (:style:) в википарсер
        """
        def __init__ (self, application):
            """
            application - экземпляр класса core.application.ApplicationParams
            """
            Plugin.__init__ (self, application)
            self.STYLE_TOOL_ID = u"PLUGIN_STYLE_TOOL_ID"


        def __onWikiParserPrepare (self, parser):
            parser.addCommand (StyleCommand (parser))


        @property
        def name (self):
            return u"Style"


        @property
        def description (self):
            return _(u"""Add command (:style:) to wiki parser. This command allow the setting of a user CSS style for a page.

<B>Usage</B>:
(:style:)
styles
(:styleend:)

<B>Example:</B>
(:style:)
body {background-color: #EEE;}
(:styleend:)
""")


        @property
        def version (self):
            return __version__


        def initialize(self):
            self._application.onWikiParserPrepare += self.__onWikiParserPrepare
            self._application.onPageViewCreate += self.__onPageViewCreate
            self._initlocale(u"style")

            if self._isCurrentWikiPage:
                self.__onPageViewCreate (self._application.selectedPage)


        def _initlocale (self, domain):
            langdir = os.path.join (os.path.dirname (__file__), "locale")
            global _

            try:
                _ = self._init_i18n (domain, langdir)
            except BaseException as e:
                print (e)


        def __onPageViewCreate(self, page):
            """Обработка события после создания представления страницы"""
            assert self._application.mainWindow is not None

            if not self._isCurrentWikiPage:
                return

            pageView = self._getPageView()

            helpString = _(u"Custom Style (:style:)")

            pageView.addTool (pageView.commandsMenu,
                              self.STYLE_TOOL_ID,
                              self.__onInsertCommand,
                              helpString,
                              helpString,
                              None)


        def __onInsertCommand (self, event):
            startCommand = u'(:style:)\n'
            endCommand = u'\n(:styleend:)'

            pageView = self._getPageView()
            pageView.codeEditor.turnText (startCommand, endCommand)


        def _getPageView (self):
            """
            Получить указатель на панель представления страницы
            """
            return self._application.mainWindow.pagePanel.pageView


        @property
        def _isCurrentWikiPage (self):
            return (self._application.selectedPage is not None and
                    self._application.selectedPage.getTypeString() == u"wiki")


        @property
        def url (self):
            return _(u"http://jenyay.net/Outwiker/StylePluginEn")


        def destroy (self):
            """
            Уничтожение (выгрузка) плагина. Здесь плагин должен отписаться от всех событий
            """
            self._application.onWikiParserPrepare -= self.__onWikiParserPrepare
            self._application.onPageViewCreate -= self.__onPageViewCreate

            if self._isCurrentWikiPage:
                self._getPageView().removeTool (self.STYLE_TOOL_ID)