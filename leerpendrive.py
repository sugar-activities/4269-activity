#! /usr/bin/env python
# Leer Pendrive
# Copyright (C) 2008 Gabriel Eirea
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Credits:
# The code used to copy to the clipboard was extracted from the Journal
# code from OLPC.
#
# Contact information:
# Gabriel Eirea geirea@gmail.com
# Ceibal Jam http://wiki.laptop.org/go/Ceibal_Jam

from sugar.activity import activity
import sys, os
import gtk, gobject
import logging

class LeerPendrive(activity.Activity):

	def __init__(self, handle):

		activity.Activity.__init__(self, handle)

		toolbox = activity.ActivityToolbox(self)
		self.set_toolbox(toolbox)
		toolbox.show()

		self._filechooser = gtk.FileChooserWidget(\
			action=gtk.FILE_CHOOSER_ACTION_OPEN,backend=None)
		self._filechooser.set_current_folder("/media")
		self.botonCopiar = gtk.Button("Copiar al portapapeles")
		self.botonCopiar.connect('clicked', self._boton_apretado)
		self.botonCopiar.show ()
		self._filechooser.set_extra_widget(self.botonCopiar)

		self.set_canvas(self._filechooser)
		self.show_all()

		toolbox.get_activity_toolbar().share.hide()
		toolbox.get_activity_toolbar().keep.hide()

	def _boton_apretado(self, widget, data=None):

		self.archivo = self._filechooser.get_filename()
		logging.info(self.archivo)
		clipboard = gtk.Clipboard()
		clipboard.set_with_data([('text/uri-list', 0, 0)],
					self._clipboard_get_func_cb,
					self._clipboard_clear_func_cb)


	def _clipboard_get_func_cb(self, clipboard, selection_data, info, data):

		selection_data.set('text/uri-list', 8, self.archivo)

	def _clipboard_clear_func_cb(self, clipboard, data):

		pass
