## ACPC Contest Data Aggregator (v1.0)
---
**Purpose**
* Used to determine who the top checked-in performers are in a Codeforces-hosted ACPC contest, both overall and by graduation year

**How to Use**
* This is an entirely offline tool. You need to download the contest sign-up spreadsheet (such as the one [here](https://docs.google.com/spreadsheets/d/1E2b4oHgNdRWvbVOO_NktqjgtFB4GkUklwyrLIMSJCXw/edit#gid=433302416)) as `signups.tsv`. The standings page for the Codeforces contest must also be downloaded as `standings.html`.
* The spreadsheet **must** have columns for the registrant's first/last name, Codeforces handle, graduation year, degree type, and whether they checked in. The names for these columns must match the pattern `*First Name*`, `*Last Name*`, `*Codeforces Handle*`, `*Graduation Year*`, `*Degree Type*`, and `*Checked In*`, respectively. The value for the checked in column must be `yes` if the registrant checked in and may be anything else (including empty) otherwise.
* Run `pip install -r requirements.txt` to make sure all Python dependencies are installed
* Make sure the downloaded files are in the same directory as `main.py`. Now, you can simply run the script. You can also run with the `-f` option and provide a filename (i.e. `python main.py -f data.out`) to write the results to a file.

**Notes**
* Make sure the spreadsheet data is not malformed for checked-in participants (this should be done when each person checks in). You will probably get incorrect results otherwise.