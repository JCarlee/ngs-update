# Ask for new folder path
# Ask for old folder path
# Create new folder \new \old
# Copy previous "new" files into "old"

import os

root = 'E:\\Planet15JCarlee\\NGS'

dirlist = [item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))]
print(max(dirlist))
