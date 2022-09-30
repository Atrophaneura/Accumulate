# main.py
#
# Copyright 2022 0xMRTT
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

from .constants import (
    rootdir,
    app_id,
    rel_ver,
    version,
    bugtracker_url,
    help_url,
    project_url,
)
from .window import MainWindow
from gi.repository import Gtk, Gio, Adw
import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')


class AccumulateApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id='io.github.Atrophaneura.Accumulate',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action('quit', self.quit, ['<primary>q'])
        self.create_action('about', self.on_about_action)
        self.create_action('preferences', self.on_preferences_action)

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(
            transient_for=self.props.active_window,
            application_name=_("Accumulate"),
            application_icon=app_id,
            developer_name=_("Atrophaneura"),
            website=project_url,
            support_url=help_url,
            issue_url=bugtracker_url,
            developers=[
                "0xMRTT https://github.com/0xMRTT",
            ],
            artists=["David Lapshin https://github.com/daudix-UFO"],
            designers=["David Lapshin https://github.com/daudix-UFO"],
            # Translators: This is a place to put your credits (formats:
            # "Name https://example.com" or "Name <email@example.com>",
            # no quotes) and is not meant to be translated literally.
            translator_credits="""0xMRTT https://github.com/0xMRTT
                David Lapshin https://github.com/daudix-UFO
            """,
            copyright="© 2022 Atrophaneura",
            license_type=Gtk.License.GPL_3_0,
            version=version,
            release_notes_version=rel_ver,
        )
        about.add_credit_section(
            "Packagers",
            [
                "0xMRTT https://github.com/0xMRTT",
            ],
        )
        about.present()

    def on_preferences_action(self, widget, _):
        """Callback for the app.preferences action."""
        print('app.preferences action activated')

    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)


def main():
    """The application's entry point."""
    app = AccumulateApplication()
    return app.run(sys.argv)
