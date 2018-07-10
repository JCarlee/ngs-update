# Ask for new folder path
# Ask for old folder path
# Create new folder \new \old
# Copy previous "new" files into "old"

import os
import datetime
now = datetime.datetime.now()

root = 'E:\\Planet15JCarlee\\NGS'

dirlist = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]

prev_month = max(dirlist)
prev_dir = root + '\\' + prev_month
new_dir = "{0}\\{1}{2}{3}".format(root, now.year, '{:02d}'.format(now.month), '{:02d}'.format(now.day))
print(new_dir)
