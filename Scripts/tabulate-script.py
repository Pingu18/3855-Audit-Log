#!"C:\Users\user\Documents\5 - Winter 2020\3855 - Service Architecture\Lab5\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'tabulate==0.8.6','console_scripts','tabulate'
__requires__ = 'tabulate==0.8.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('tabulate==0.8.6', 'console_scripts', 'tabulate')()
    )
