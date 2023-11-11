## ACPC Contest Data Aggregator (v1.0)
---
**Purpose**
* Used to determine who the top checked-in performers are in a Codeforces-hosted ACPC contest, both overall and by graduation year

**How to Use**
* This is an entirely offline tool. You need to download the contest sign-up spreadsheet (such as the one [here](https://docs.google.com/spreadsheets/d/1E2b4oHgNdRWvbVOO_NktqjgtFB4GkUklwyrLIMSJCXw/edit#gid=433302416)) as a `.csv`. The standings page for the Codeforces contest must also be downloaded as a `.html`.
* The spreadsheet **must** have columns for the registrant's Codeforces handle, graduation year, and whether they checked in. The names for these columns must match the pattern `*Codeforces Handle*`, `*Graduation Year*`, and `*Checked In*`, respectively. The value for the checked in column must be `yes` if the registrant checked in and may be anything else (including empty) otherwise.
* Make sure the downloaded files are in the same directory as `main.py`. Now, you can simply run the script. You can also run with the `-f` option and provide a filename (i.e. `python main.py -f data.out`) to write the results to a file.

**Notes**
* Make sure the spreadsheet data is 