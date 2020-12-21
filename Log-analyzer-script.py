import socket
from collections import Counter
from pip._vendor.distlib.compat import raw_input

line_count = 0
columns_count = 0
request_success_count = 0
request_error_count = 0
top_pages = {}
top_domains = {}
error_domains = {}
top_pages_sum = {}

with open("access_log_Aug95") as infile:
    for line in infile:
        columns = line.split()
        columns_count = len(columns)
        line_count = line_count + 1
        # 1st
        top_pages.update({columns[0] + columns[6]: top_pages.get(columns[0] + columns[6], 0) + 1})
        #2nd-3rd
        response_code = int(columns[columns_count-2])
        if response_code >= 200 and response_code < 300:
            request_success_count = request_success_count + 1
        else:
            request_error_count = request_error_count + 1
        #4th
        if response_code >= 300:
            error_domains.update({columns[0]: error_domains.get(columns[0], 0) + 1})
        #5st
        top_domains.update({columns[0]: top_domains.get(columns[0], 0) + 1})
        #6th
        top_pages_sum.update({columns[6]: top_pages_sum.get(columns[6], 0) + 1})


#1st
def task1():
    print("Top 10 requested pages and the number of requests made for each: ")
    counted = Counter(top_pages)
    most_common = counted.most_common(10)
    for k, v in counted.most_common(10):
        print(k, v)

def task1_1():
    print("Top 10 requested pages: ")
    counted = Counter(top_pages_sum)
    most_common = counted.most_common(10)
    for k, v in counted.most_common(10):
        print(k)

#2nd
def task2():
    rsc = (request_success_count / line_count) * 100
    print("Percentage of successful requests (anything in the 200s and 300s range): ", '{0:.2f}%'.format(rsc))

#3rd
def task3():
    print("Percentage of unsuccessful requests (anything that is not in the 200s or 300s range): "'{0:.2f}%'.format((request_error_count / line_count) * 100))

#4th
def task4():
    print("Top 10 unsuccessful page requests :")
    for k, v in Counter(error_domains).most_common(10):
        print(k, v)

def task4_4():
    print("Top 10 unsuccessful page requests :")
    for k, v in Counter(error_domains).most_common(10):
        print(k)

#5th
def task5():
    print("The top 10 hosts making the most requests, displaying the IP address and number of requests made :")
    counted = Counter(top_domains)
    most_common = counted.most_common(10)
    for k, v in counted.most_common(10):
        print(k, v)
        try:
            print(socket.gethostbyname(k))
        except:
            print("No ip for ",k)

def task6():
    print("Option parsing to produce only the report for one of the previous points (e.g. only the top 10 urls, only the percentage of successful requests and so on) :")
    task1_1()
    task2()
    task3()
    task4_4()

def task7():
    print("Print README file:")
    file = open("README.md", "r")
    print(file.read())

def task8():
    print("Test - out of order :")

def task9():
    print("For each of the top 10 hosts, show the top 5 pages requested and the number of requests for each :")
    for k, v in Counter(top_domains).most_common(10):
        print(k, v)
        top_domain_pages = {key: value for (key, value) in top_pages.items() if key.startswith(k)}
        for kk, vv in Counter(top_domain_pages).most_common(5):
            print(kk, vv)

ans=True
while ans:
    print("""
    1. Top 10 requested pages and the number of requests made for each
    2. Percentage of successful requests (anything in the 200s and 300s range)
    3. Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
    5. The top 10 hosts making the most requests, displaying the IP address and number of requests made
    6. Option parsing to produce only the report for one of the previous points (e.g. only the top 10 urls, only the percentage of successful requests and so on)
    7. Print README file
    8. Test (out of order)
    9. For each of the top 10 hosts, show the top 5 pages requested and the number of requests for each
    10. Exit/Quit
    """)
    ans=raw_input("What would you like to do? ")
    if ans=="1":
      task1()
    elif ans=="2":
      task2()
    elif ans=="3":
      task3()
    elif ans=="4":
      task4()
    elif ans=="5":
      task5()
    elif ans=="6":
      task6()
    elif ans=="7":
      task7()
    elif ans=="8":
      task8()
    elif ans=="9":
      task9()
    elif ans=="10":
      print("\n Goodbye")
      ans = None
    else:
       print("\n Not Valid Choice Try again")
