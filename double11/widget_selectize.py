# coding=utf-8

from IPython.html.widgets import Select
from IPython.utils.traitlets import (Unicode, CaselessStrEnum, Bool)


class SelectizeWidget(Select):
    _view_name = Unicode('SelectizeView', sync=True)
    theme = CaselessStrEnum(
        values=['default', 'legacy', 'bootstrap2', 'bootstrap3'],
        default_value='default', sync=True,
        help="""Use a them styling for the SelectizeWidget.""")
    disabled = Bool(False, help="Enable or disable user changes", sync=True)
    description = Unicode(
        help="Description of the value this widget represents", sync=True)

    def __init__(self, *args, **kwargs):
        Select.__init__(self, *args, **kwargs)
        self.value = ','.join(self.values)

    def _value_name_changed(self, name, old, new):
        """Called when the value name has been changed
           (typically by the frontend)."""
        if self.value_lock.acquire(False):
            try:
                self.value_name = self.value = new
            finally:
                self.value_lock.release()

    def _value_changed(self, name, old, new):
        """Called when value has been changed"""
        if self.value_lock.acquire(False):
            try:
                self.value_name = self.value = new
            finally:
                self.value_lock.release()
