config.load_autoconfig(False)
config.set('content.cookies.accept', 'all', 'chrome-devtools://*')
config.set('content.cookies.accept', 'all', 'devtools://*')
c.content.fullscreen.window = True
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')
c.tabs.show = 'never'
c.colors.webpage.darkmode.enabled = False
c.fonts.statusbar = '6'





config.set(
    "url.searchengines",
    {
        "DEFAULT": "https://duckduckgo.com/?q={}",
        "sp": "https://www.startpage.com/do/search?query={}",
        "g": "https://www.google.com/search?q={}",
        "d": "https://duckduckgo.com/?q={}",
        "di": "https://duckduckgo.com/?ia=images&iax=images&q={}",
        "qw": "https://qwant.com/?q={}&t=web",
        "qwi": "https://qwant.com/?q={}&t=images",
        "gi": "https://www.google.com/search?q={}&tbm=isch",
        "map": "https://www.google.com/maps/?q={}",
        "twi": "https://twitter.com/search?q={}",
        "yt": "https://youtube.com/results?search_query={}",
        "aur": "https://aur.archlinux.org/packages/?K={}",
        "arch": "https://www.archlinux.org/packages/?q={}",
        "wiki": "https://www.wikipedia.org/w/index.php?search={}",
        "git": "https://github.com/search?q={}",
        "deal": "https://www.dealabs.com/search?q={}",
        "protondb": "https://www.protondb.com/search?q={}",
        "archwiki": "https://wiki.archlinux.org/index.php?search={}",
        "reddit": "https://www.reddit.com/search?q={}&sort=relevance&t=all",
        "subreddit": "https://www.reddit.com/r/{}",
        "scholar": "https://scholar.google./scholar?hl=fr&q={}",
        "libgen": "http://www.libgen.is/search.php?req={}",
        "scihub": "https://sci-hub.tw/{}",
        "trend": "https://trends.google.fr/trends/explore?q={}",
        "stack": "https://stackoverflow.com/search?q={}",
        "osm": "https://www.openstreetmap.org/search?query={}",
        "goodreads": "https://www.goodreads.com/search?q={}",
        "pypi": "https://pypi.org/search/?q={}",
        "openrepos": "https://openrepos.net/search/node/{}",
        "unsplash": "https://unsplash.com/search/photos/{}",
        "alternativeto": "https://alternativeto.net/software/{}",
        "gitlab": "https://gitlab.com/search?search={}",
        
        'doc':'hwttps://devdocs.io/#q={}',
        'ddgl':'https://lite.duckduckgo.com/?q={}',
        'qwl':'https://lite.qwant.com/?q={}',
        'sx':'https://searx.info/search?q={}&language=en-US',
        'sw':'https://swisscows.com/web?region=iv&query={}',
        'wi':'https://wiby.me/?q={}',
    },
)

# video autoplay
c.content.autoplay = False

# geolocation
c.content.geolocation = False

# canvas
c.content.canvas_reading = False

# webgl
c.content.webgl = False

# wbrtc
c.content.webrtc_ip_handling_policy = 'default-public-interface-only'

# cookies
c.content.cookies.accept = 'no-3rdparty'






palette = {
    'background': '#000000',
    'background-alt': '#101000',
    'background-attention': '#181920',
    'border': '#282a36',
    'current-line': '#44475a',
    'selection': '#44475a',
    'foreground': '#868682',
    'foreground-alt': '#e0e0e0',
    'foreground-attention': '#ffffff',
    'comment': '#6272a4',
    'cyan': '#8be9fd',
    'green': '#50fa7b',
    'orange': '#ffb86c',
    'pink': '#ff79c6',
    'purple': '#bd93f9',
    'red': '#ff5555',
    'yellow': '#f1fa8c'
}
spacing = {
    'vertical': 2,
    'horizontal': 2
}
padding = {
    'top': spacing['vertical'],
    'right': spacing['horizontal'],
    'bottom': spacing['vertical'],
    'left': spacing['horizontal']
}

# Background color of the completion widget category headers.
c.colors.completion.category.bg = palette['background']

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = palette['border']

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = palette['border']

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = palette['foreground']

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = palette['background']

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = palette['background-alt']

# Text color of the completion widget.
c.colors.completion.fg = palette['foreground']

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = palette['selection']

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = palette['selection']

# Top border color of the completion widget category headers.
c.colors.completion.item.selected.border.top = palette['selection']

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = palette['foreground']

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = palette['orange']

# Color of the scrollbar in completion view
c.colors.completion.scrollbar.bg = palette['background']

# Color of the scrollbar handle in completion view.
c.colors.completion.scrollbar.fg = palette['foreground']

# Background color for the download bar.
c.colors.downloads.bar.bg = palette['background']

# Background color for downloads with errors.
c.colors.downloads.error.bg = palette['background']

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = palette['red']

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = palette['background']

# Color gradient interpolation system for download backgrounds.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = palette['background']

# Font color for hints.
c.colors.hints.fg = palette['purple']

# Hints
c.hints.border = '1px solid ' + palette['background-alt']

# Font color for the matched part of hints.
c.colors.hints.match.fg = palette['foreground-alt']

# Background color of the keyhint widget.
c.colors.keyhint.bg = palette['background']

# Text color for the keyhint widget.
c.colors.keyhint.fg = palette['purple']

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = palette['selection']

# Background color of an error message.
c.colors.messages.error.bg = palette['background']

# Border color of an error message.
c.colors.messages.error.border = palette['background-alt']

# Foreground color of an error message.
c.colors.messages.error.fg = palette['red']

# Background color of an info message.
c.colors.messages.info.bg = palette['background']

# Border color of an info message.
c.colors.messages.info.border = palette['background-alt']

# Foreground color an info message.
c.colors.messages.info.fg = palette['comment']

# Background color of a warning message.
c.colors.messages.warning.bg = palette['background']

# Border color of a warning message.
c.colors.messages.warning.border = palette['background-alt']

# Foreground color a warning message.
c.colors.messages.warning.fg = palette['red']

# Background color for prompts.
c.colors.prompts.bg = palette['background']

# Border used around UI elements in prompts.
c.colors.prompts.border = '1px solid ' + palette['background-alt']

# Foreground color for prompts.
c.colors.prompts.fg = palette['cyan']

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = palette['selection']

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = palette['background']

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = palette['orange']

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = palette['background']

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = palette['orange']

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = palette['background']

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = palette['foreground'] 

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = palette['background']

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = palette['foreground-alt']

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = palette['background-attention']

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = palette['foreground-attention']

# Background color of the statusbar.
c.colors.statusbar.normal.bg = palette['background']

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = palette['foreground']

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = palette['background']

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = palette['orange']

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = palette['background-alt']

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = palette['foreground-alt']

# Background color of the progress bar.
c.colors.statusbar.progress.bg = palette['background']

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = palette['red']

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = palette['foreground']

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = palette['cyan']

# Foreground color of the URL in the statusbar on successful load
c.colors.statusbar.url.success.http.fg = palette['green']

# Foreground color of the URL in the statusbar on successful load
c.colors.statusbar.url.success.https.fg = palette['green']

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = palette['yellow']

# Status bar padding
c.statusbar.padding = padding




c.statusbar.show = 'in-mode'
#how blank page when opening new page
c.url.default_page = 'about:blank'
c.url.start_pages = ['about:blank']

c.completion.shrink = True
c.completion.use_best_match = True
config.bind('x','config-cycle statusbar.show always never')
