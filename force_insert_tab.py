
import sublime
import sublime_plugin

# https://stackoverflow.com/questions/45587788/sublime-text-3-insert-tab-character-manually
# https://forum.sublimetext.com/t/insert-tab-characters-but-indent-using-spaces/9043/8
# https://superuser.com/questions/776192/how-to-insert-a-tab-character-in-sublime-text
class RichPlainTextForceInsertTabCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        settings = view.settings()

        translate_tabs_to_spaces = settings.get('translate_tabs_to_spaces', True)
        if translate_tabs_to_spaces: settings.set('translate_tabs_to_spaces', False)

        for selection in view.sel():
            view.insert(edit, selection.a, '\t')

        if translate_tabs_to_spaces: settings.set('translate_tabs_to_spaces', True)


class RichPlainTextForceInsertNewlineCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        settings = view.settings()

        auto_indent = settings.get('auto_indent', True)
        if auto_indent: settings.set('auto_indent', False)

        for selection in view.sel():
            view.insert(edit, selection.a, '\n')

        if auto_indent: settings.set('auto_indent', True)

