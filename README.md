# ngs-update

Create current month's directory along with 'new' and 'old' folders. Copy previous month's dbf files into current 'old' folder. Download all ZIP files from NOAA FTP into 'new' folder.

Working directory is hardcoded to "E:\Planet15JCarlee\NGS\Files" making this tool only functional on John Carlee's workstation at uGRIDD. This can be easily adapted to a different machine by changing line 9 to preferred local path.

Script is scheduled to run on the first day of every month at 9:00 AM CDT.

Following completion of script, run the dbf2Sql utility to complete the NGS update process.

Please contact John Carlee at JCarlee@gmail.com with any questions.
