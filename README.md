# ngs-update

Utility to aid uGRIDD's monthly NGS Monument update.

Create current month's directory along with 'new' and 'old' folders. Copy previous month's dbf files into current 'old' folder. Download all ZIP files from NOAA FTP into 'new' folder.

## Dependencies
* Python 3.6
* os
* datetime
* shutil
* FTP/ftplib 

## Getting Started
Working directory is hardcoded to "E:\Planet15JCarlee\NGS\Files" making this tool only functional on John Carlee's workstation at uGRIDD. This can be easily adapted to a different machine by changing line 9 to preferred local path.

### Scheduling

Schedule to run on the first day of every month at 9:00 AM CDT.
* Type "Task Scheduler" into windows search bar
* Open Task Scheduler
* Under **Actions** side bar, select *Create Basic Task*
* Enter a logical Name, Next
* Select monthly
* Set time, select all months, set Days to 1
* Start a program
* Program/script is the python.exe path
* Add arguments: "C:\YOUR_DIRECTORY\ngs-script.py"

### Completing the Update

Following completion of script, run the internal dbf2Sql utility to complete the NGS update process.

## Author

* **John Carlee** - JCarlee@gmail.com
