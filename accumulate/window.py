# window.py
#
# Copyright 2022 Atrophaneura
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

from ast import Gt
from gi.repository import Gtk, Adw, Gio

from .constants import rootdir, app_id


@Gtk.Template(resource_path=f'{rootdir}/ui/window.ui')
class AccumulateWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'AccumulateWindow'

    main_view = Gtk.Template.Child()
    main = Gtk.Template.Child()
    bottom_bar = Gtk.Template.Child()
    send_button = Gtk.Template.Child()
    view_stack = Gtk.Template.Child()
    success = Gtk.Template.Child()
    main = Gtk.Template.Child()
    content = Gtk.Template.Child()
    
    settings = Gio.Settings(app_id)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def save_window_props(self, *args):
        win_size = self.get_default_size()

        self.settings.set_int("window-width", win_size.width)
        self.settings.set_int("window-height", win_size.height)

        self.settings.set_boolean("window-maximized", self.is_maximized())
        self.settings.set_boolean("window-fullscreen", self.is_fullscreen())

