from typing import Set

BROWSER_NAMES=set(['msedge.exe','chrome.exe','firefox.exe'])

AVOIDED_APPS:Set[str]=set([
    'Recording toolbar'
])

EXCLUDED_CLASSNAMES:Set[str]=set([
    'Progman','Shell_TrayWnd','Microsoft.UI.Content.PopupWindowSiteBridge'
])