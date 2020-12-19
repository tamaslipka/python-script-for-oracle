# python
HTTP log file parsing

This tool can analyze the following exact log file: access_log_Aug95

The log file is reachable on the following url: ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz

Preconditions:
Python 2.7.17 min. required
Extract and copy NASA_access_log_Aug95 file into the python project folder
Start Log-analyzer-script.py and choose from the following options:

Using the sample log file, perform the following tasks:
1. Top 10 requested pages and the number of requests made for each
2. Percentage of successful requests (anything in the 200s and 300s range)
3. Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
4. Top 10 unsuccessful page requests
5. The top 10 hosts making the most requests, displaying the IP address and number of requests made.
6. Option parsing to produce only the report for one of the previous points (e.g. only the top 10 urls, only the percentage of successful requests and so on)
7. A README file explaining how to use the tool, what its dependencies and any assumptions you made while writing it

Extra points will be given for:
8. Tests
9. For each of the top 10 hosts, show the top 5 pages requested and the number of requests for each
