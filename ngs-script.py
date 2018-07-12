# Create new folder \new \old
# Copy previous "new" files into "old"

import os
import datetime
import shutil
from ftplib import FTP


class MyClass(object):
    def __init__(self):
        self.root = 'E:\\Planet15JCarlee\\NGS\\Files'
        self.now = datetime.datetime.now()
        self.new_dir = "{0}\\{1}{2}{3}".format(self.root, self.now.year,
                                               '{:02d}'.format(self.now.month), '{:02d}'.format(self.now.day))
        self.new_dir_new = self.new_dir + "\\new"
        self.new_dir_old = self.new_dir + "\\old"
        self.new_dir_output = self.new_dir + "\\output"
        self.dirlist = [item for item in os.listdir(self.root) if os.path.isdir(os.path.join(self.root, item))]
        self.prev_month = max(self.dirlist)  # Previous month's folder name
        self.prev_dir_new = self.root + '\\' + self.prev_month + '\\new'  # Previous month's new folder
        self.source = os.listdir(self.prev_dir_new)  # Create list from previous month's

    def dir_move(self):
        # Create new month root directory
        if not os.path.exists(self.new_dir):
            os.makedirs(self.new_dir)

        # Create new-new directory
        if not os.path.exists(self.new_dir_new):
            os.makedirs(self.new_dir_new)
            print("CREATED: " + self.new_dir_new)

        # Create new-old directory
        if not os.path.exists(self.new_dir_old):
            os.makedirs(self.new_dir_old)
            print("CREATED: " + self.new_dir_old)

        # Create new-output directory
        if not os.path.exists(self.new_dir_output):
            os.makedirs(self.new_dir_output)
            print("CREATED: " + self.new_dir_output)

        # Copy old dbf files into new-old directory
        for files in self.source:
            if files.endswith(".dbf"):
                shutil.copy(self.prev_dir_new + '\\' + files, self.new_dir_old)

        print("Copied .dbf files from {0} to {1}".format(self.prev_dir_new, self.new_dir_old))

    def ftp_dl(self):
        ftp = FTP("ftp.ngs.noaa.gov", "anonymous")  # Define FTP credentials
        ftp.login()
        ftp.cwd("/pub/DS_ARCHIVE/ShapeFiles")  # Change directory
        root_dirs = ftp.nlst()
        root_dirs.remove('ARCHIVE')

        for i in root_dirs:
            print(i + " downloading " + str(ftp.size(i)) + " bytes")
            local_filename = os.path.join(self.new_dir_new, i)
            fh = open(local_filename, 'wb')
            ftp.retrbinary('RETR ' + i, fh.write)  # Download current file in loop
            print(i + " download complete")
        ftp.close()


a = MyClass()
a.dir_move()
a.ftp_dl()
