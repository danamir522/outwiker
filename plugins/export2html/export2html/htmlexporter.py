#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os.path

from BeautifulSoup import BeautifulSoup

from .exceptions import HtmlNotFoundError
from .baseexporter import BaseExporter


class HtmlExporter (BaseExporter):
    """
    Класс для экспорта HTML- и викистраниц
    """
    def export (self, page, outdir, imagesonly, alwaisOverwrite):
        """
        Экспорт HTML-страниц
        """
        assert (page.getTypeString() == "html" or 
                page.getTypeString() == "wiki" )

        self.__htmlFileName = u"__content.html"

        # Чтение файла с содержимым
        try:
            with open (os.path.join (page.path, self.__htmlFileName) ) as fp:
                content = unicode (fp.read(), "utf8")
        except IOError:
            raise HtmlNotFoundError (_(u"{0} not found").format (self.__htmlFileName) )

        changedContent = self.__prepareHtmlContent (content, page.title)
        exportname = page.title

        self._exportContent (page, 
                changedContent,
                exportname,
                outdir,
                imagesonly,
                alwaisOverwrite)


    def __replaceAttaches (self, tags, attrib, pagetitle):
        """
        Заменить ссылки на папку __attach на новую папку с вложениями
        """
        self.__attachDir = "__attach"

        for tag in tags:
            if tag.has_key (attrib) and tag[attrib].startswith (self.__attachDir):
                tag[attrib] = tag[attrib].replace (self.__attachDir, pagetitle, 1)


    def __prepareHtmlContent (self, content, pagetitle):
        """
        Заменить ссылки на прикрепленные файлы
        Используется при экспорте HTML-страниц
        """
        soup = BeautifulSoup (content)
        images = soup.findAll ("img")
        self.__replaceAttaches (images, "src", pagetitle)

        links = soup.findAll ("a")
        self.__replaceAttaches (links, "href", pagetitle)

        return unicode (soup.renderContents(), "utf8")
