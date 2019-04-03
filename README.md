# ngs-update

Utility to aid monthly NGS Monument updates.

Create current month's directory along with 'new' and 'old' folders. Copy previous month's dbf files into current 'old' folder. Download all ZIP files from NOAA FTP into 'new' folder.

## Author
**John Carlee** - JCarlee@gmail.com

I am 9 year veteran in the Geographic Information Science and Cartography space. **I am currently looking for new job 
opportunities leveraging my GIS skills with a heavy focus on Python development.**


## Dependencies
* Python 3
* os
* datetime
* shutil
* FTP/ftplib 

## Getting Started
Place ngs-script.py into your working directory.

### Scheduling

Schedule to run on the first day of every month at 9:00 AM CDT.
* Type "Task Scheduler" into windows search bar
* Open Task Scheduler
* Under **Actions** side bar, select *Create Basic Task*
* Enter a Name
* Select monthly
* Set time, select all months, set Days to 1
* Start a program
* Program/script is the python.exe path (C:\Users\JoeSmith\AppData\Local\Programs\Python\Python37-32\python.exe)
* Add arguments: C:\[YOUR_DIRECTORY]\ngs-script.py

### Completing the Update

Following completion of script, run the internal dbf2Sql utility to complete the NGS update process (or add to scheduled task).
