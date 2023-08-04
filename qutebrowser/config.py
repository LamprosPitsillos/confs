config.load_autoconfig(True)
c.fonts.tabs.selected = "default_size Fira Code Bold"
c.fonts.tabs.unselected = "default_size Fira Code Bold"
c.backend = "webengine"
c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "y": "https://www.youtube.com/results?search_query={}",
    "gt": "https://github.com/search?q={}",
    "g": "https://www.google.com/search?q={}",
    "st":"https://stackoverflow.com/search?q={}",
        "CPP":"https://duckduckgo.com/?sites=cppreference.com&q={}"
}
c.content.javascript.can_access_clipboard = True
c.aliases = {
    "w": "session-save",
    "q": "close",
    "qa": "quit",
    "wq": "quit --save",
    "wqa": "quit --save",
}
c.confirm_quit = ["always"]
c.editor.command = ["kitty", "-e", "nvim", "{}","+'set filetype=markdown'"]
c.scrolling.smooth = True
c.spellcheck.languages = ["el-GR", "en-US"]
c.statusbar.show = "always"
c.completion.height = "35%"
c.tabs.show = "multiple"
c.tabs.background = True
c.zoom.mouse_divider = 10
leader = ","
config.bind('<Escape>', 'mode-leave ;; jseval -q document.activeElement.blur()', mode='insert')
config.bind(
        "sp", "set-cmd-text :print --pdf ~/downs/"
)

config.bind(
    "cb", "set colors.webpage.bg white"
)
config.bind(
    "<Ctrl-o>" + "y", "open -t www.youtube.com"
)
config.bind(
    "<Ctrl-o>" + "g", "open -t www.github.com"
)
config.bind(
    "<Ctrl-o>" + "f", "open -t www.facebook.com/messages/"
)
config.unbind("?", mode="normal")
config.bind( "?", "search {primary}"
)
config.bind(
    leader + "v", "hint links spawn --detach mpv --ytdl --force-window=immediate {hint-url}"
)
config.bind(
    leader + "V", "spawn --detach --verbose mpv --ytdl --force-window=immediate {url}"
)
config.bind(
    leader + "m", "hint links spawn --detach mpv --ytdl --no-video --force-window=immediate {hint-url}"
)
config.bind(
    leader + "M", "spawn --detach --verbose mpv --ytdl --no-video --force-window=immediate {url}"
)
config.bind(
    leader + "dm",
    'hint links spawn --verbose yt-dlp -x {hint-url} --embed-thumbnail --embed-metadata --audio-format mp3 --audio-quality 0 -o "$HOME/music/%(artist)s/%(title)s.%(ext)s" ',
)
config.bind(
    leader + "dM",
    'spawn --verbose yt-dlp -x {url} --embed-thumbnail --embed-metadata --audio-format mp3 --audio-quality 0 -o "$HOME/music/%(artist)s/%(title)s.%(ext)s" ',
)
config.bind(
    leader + "dv",
    "hint links spawn --verbose yt-dlp {hint-url} --embed-thumbnail -o ~/vids/%(title)s.%(ext)s",
)
config.bind(
    leader + "dV",
    "spawn --verbose yt-dlp {url} --embed-thumbnail -o ~/vids/%(title)s.%(ext)s",
)
config.bind(
   "py",
    'open -- y {primary}',
)
config.bind(
   "PY",
    'open -t -- y {primary}',
)
config.bind('yy', 'yank -s')
config.bind('yY', 'yank')
# config.bind(
#     leader + "w",
#     "hint links spawn --verbose wget --directory-prefix=/home/inferno/downs/Wget {hint-url}",
# )
# config.bind(
#     leader + "W",
#     "spawn --verbose wget --directory-prefix=/home/inferno/downs/Wget {url}",
# )
config.bind(leader + "dp", "spawn git clone {url} ~/docs/Packages/")
config.bind(leader + "c", "spawn --userscript credentials.sh")
config.bind(leader + "y", "open -t -- y {primary}")
config.bind(leader + "p", "hint links run open -p {hint-url}")
config.bind(leader + "P", "open -p")
config.bind(leader + "D" ,"open -t https://www.dictionary.com/browse/{primary}")
config.bind(leader + "T" ,"open -t https://translate.google.com/?sl=en&tl=el&text={primary}%0A&op=translate")

config.bind("es", "spawn kitty nvim /tmp/qute_sel -c 'norm p'")
config.bind("ec", "config-edit")
config.bind("eu", "edit-url")
config.bind("W", "hint all window")
config.bind("I", "hint inputs")
config.unbind("d", mode="normal")
config.bind("dd", "tab-close")
config.bind("<Alt-k>", "tab-next")
config.bind("<Alt-j>", "tab-prev")
# c.content.pdfjs = True
c.content.blocking.adblock.lists = [
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
    "https://easylist.to/easylist/fanboy-annoyance.txt",
    "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
    "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
]
c.content.blocking.method = "both"
c.tabs.title.format = "{index}: {current_title} {audio}{private}"
palette = {
    "background": "#1c1c1c",
    "background-alt": "#161616",
    "background-attention": "#181920",
    "border": "#282a36",
    "gray": "#909497",
    "selection": "#333333",
    "foreground": "#f8f8f2",
    "foreground-alt": "#e0e0e0",
    "foreground-attention": "#ffffff",
    "comment": "#6272a4",
    "cyan": "#8be9fd",
    "green": "#50fa7b",
    "orange": "#ffb86c",
    "pink": "#ff79c6",
    "brown": "#ffaf00",
    "purple": "#bd93f9",
    "red": "#ff5555",
    "yellow": "#f1fa8c",
}


c.colors.webpage.bg = '#333333'
## Background color of the completion widget category headers.
c.colors.completion.category.bg = palette["background"]

## Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = palette["border"]

## Top border color of the completion widget category headers.
c.colors.completion.category.border.top = palette["border"]

## Foreground color of completion widget category headers.
c.colors.completion.category.fg = palette["foreground"]

## Background color of the completion widget for even rows.
c.colors.completion.even.bg = palette["background"]

## Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = palette["background-alt"]

## Text color of the completion widget.
c.colors.completion.fg = palette["foreground"]

## Background color of the selected completion item.
c.colors.completion.item.selected.bg = palette["selection"]

## Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = palette["selection"]

## Top border color of the completion widget category headers.
c.colors.completion.item.selected.border.top = palette["selection"]

## Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = palette["foreground"]

## Foreground color of the matched text in the completion.
c.colors.completion.match.fg = palette["orange"]

## Color of the scrollbar in completion view
c.colors.completion.scrollbar.bg = palette["background"]

## Color of the scrollbar handle in completion view.
c.colors.completion.scrollbar.fg = palette["foreground"]

## Background color for the download bar.
c.colors.downloads.bar.bg = palette["background"]

## Background color for downloads with errors.
c.colors.downloads.error.bg = palette["background"]

## Foreground color for downloads with errors.
c.colors.downloads.error.fg = palette["red"]

## Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = palette["background"]

## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.downloads.system.bg = "none"

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
c.colors.hints.bg = palette["background"]

## Font color for hints.
c.colors.hints.fg = palette["foreground-attention"]

## Hints
c.hints.border = "1px solid " + palette["background-alt"]

## Font color for the matched part of hints.
c.colors.hints.match.fg = palette["foreground-alt"]

## Background color of the keyhint widget.
c.colors.keyhint.bg = palette["background"]

## Text color for the keyhint widget.
c.colors.keyhint.fg = palette["gray"]

## Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = palette["foreground-attention"]

## Background color of an error message.
c.colors.messages.error.bg = palette["background"]

## Border color of an error message.
c.colors.messages.error.border = palette["background-alt"]

## Foreground color of an error message.
c.colors.messages.error.fg = palette["red"]

## Background color of an info message.
c.colors.messages.info.bg = palette["background"]

## Border color of an info message.
c.colors.messages.info.border = palette["background-alt"]

## Foreground color an info message.
c.colors.messages.info.fg = palette["foreground-attention"]

## Background color of a warning message.
c.colors.messages.warning.bg = palette["background"]

## Border color of a warning message.
c.colors.messages.warning.border = palette["background-alt"]

## Foreground color a warning message.
c.colors.messages.warning.fg = palette["red"]

## Background color for prompts.
c.colors.prompts.bg = palette["background"]

# ## Border used around UI elements in prompts.
c.colors.prompts.border = "1px solid " + palette["background"]

## Foreground color for prompts.
c.colors.prompts.fg = palette["orange"]

## Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = palette["selection"]

## Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = palette["background"]

## Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = palette["orange"]

## Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = palette["background"]

## Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = palette["orange"]

## Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = palette["background"]

## Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = palette["brown"]

## Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = palette["background"]

## Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = palette["foreground-alt"]

## Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = palette["background-attention"]

## Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = palette["foreground-attention"]

## Background color of the statusbar.
c.colors.statusbar.normal.bg = palette["background"]

## Foreground color of the statusbar.
c.colors.statusbar.normal.fg = palette["foreground"]

## Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = palette["background"]

## Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = palette["orange"]

## Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = palette["background-alt"]

## Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = palette["foreground-alt"]

## Background color of the progress bar.
c.colors.statusbar.progress.bg = palette["background"]

## Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = palette["red"]

## Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = palette["foreground"]

## Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = palette["cyan"]

## Foreground color of the URL in the statusbar on successful load
c.colors.statusbar.url.success.http.fg = palette["green"]

## Foreground color of the URL in the statusbar on successful load
c.colors.statusbar.url.success.https.fg = palette["green"]

## Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = palette["yellow"]

## Background color of the tab bar.
## Type: QtColor
c.colors.tabs.bar.bg = palette["selection"]

## Background color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.bg = palette["selection"]

## Foreground color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.fg = palette["foreground"]

## Color for the tab indicator on errors.
## Type: QtColor
c.colors.tabs.indicator.error = palette["red"]

## Color gradient start for the tab indicator.
## Type: QtColor
c.colors.tabs.indicator.start = palette["orange"]

## Color gradient end for the tab indicator.
## Type: QtColor
c.colors.tabs.indicator.stop = palette["green"]

## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.tabs.indicator.system = "none"

## Background color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.bg = palette["selection"]

## Foreground color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.fg = palette["foreground"]

# ## Background color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.bg = palette["background"]

# ## Foreground color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.fg = palette["brown"]

# ## Background color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.bg = palette["background"]

# ## Foreground color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.fg = palette["brown"]

## Tab padding
c.tabs.indicator.width = 1
c.tabs.favicons.scale = 1
