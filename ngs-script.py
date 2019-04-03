import os
import datetime
import shutil
from ftplib import FTP


class NGS(object):
    def __init__(self):
        self.root = os.getcwd()
        self.now = datetime.datetime.now()

        # Define current month directory path
        self.new_dir = "{0}\\{1}{2}{3}"\
            .format(self.root, self.now.year, '{:02d}'.format(self.now.month), '{:02d}'.format(self.now.day))

        self.new_dir_new = self.new_dir + "\\new"
        self.new_dir_old = self.new_dir + "\\old"

        # Create list of directories that exist in root
        self.dirlist = [item for item in os.listdir(self.root) if os.path.isdir(os.path.join(self.root, item))]

        self.prev_month = max(self.dirlist)                               # Previous month's folder name
        self.prev_dir_new = self.root + '\\' + self.prev_month + '\\new'  # Previous month's new folder
        self.source = os.listdir(self.prev_dir_new)                       # Create list from previous month's

    def dir_copy(self):
        if not os.path.exists(self.new_dir):        # Create new month root directory
            os.makedirs(self.new_dir)

        if not os.path.exists(self.new_dir_new):    # Create new-new directory
            os.makedirs(self.new_dir_new)
            # print("CREATED: " + self.new_dir_new)

        if not os.path.exists(self.new_dir_old):    # Create new-old directory
            os.makedirs(self.new_dir_old)
            # print("CREATED: " + self.new_dir_old)

        for files in self.source:                   # Copy old dbf files into new-old directory
            if files.endswith(".dbf"):
                shutil.copy(self.prev_dir_new + '\\' + files, self.new_dir_old)

        # print("Copied .dbf files from {0} to {1}".format(self.prev_dir_new, self.new_dir_old))

    def ftp_dl(self):                               # Function to download zip files from FTP
        ftp = FTP("ftp.ngs.noaa.gov", "anonymous")  # Define FTP credentials
        ftp.login()                                 # Login using credentials
        ftp.cwd("/pub/DS_ARCHIVE/ShapeFiles")       # Change directory to shapefiles
        root_dirs = ftp.nlst()                      # Create list of files in FTP directory
        root_dirs.remove('ARCHIVE')                 # Remove folder 'ARCHIVE' from the list

        for i in root_dirs:                         # Loop through items in FTP dir, downloading each to new-new dir
            # print(i + " downloading " + str(ftp.size(i)) + " bytes")
            local_filename = os.path.join(self.new_dir_new, i)
            fh = open(local_filename, 'wb')
            ftp.retrbinary('RETR ' + i, fh.write)   # Download current file in loop
            # print(i + " download complete")
        ftp.close()


a = NGS()
a.dir_copy()
a.ftp_dl()
