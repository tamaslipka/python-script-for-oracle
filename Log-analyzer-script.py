from collections import Counter

line_count = 0
request_success_count = 0
request_error_count = 0
top_domains = {}
error_domains = {}

with open("c:\\Users\\Tamas_Lipka\\Downloads\\Oracle\\access_log_Aug95") as infile:
    for line in infile:
        columns = line.split()
        cloumns_count = len(columns)

        # 1st
        top_domains.update({columns[0]: top_domains.get(columns[0], 0) + 1})

        #2nd
        response_code =int(columns[cloumns_count-2])
        line_count = line_count + 1
        if response_code >= 200 and response_code < 300:
            request_success_count = request_success_count +1
        else:
            request_error_count = request_error_count + 1

        #3rd
        if response_code >= 300:
            error_domains.update({columns[0]: error_domains.get(columns[0], 0) + 1})

#1st
counted = Counter(top_domains)
mostcommon = counted.most_common(10)
for k, v in counted.most_common(10):
    print(k, v)
#3rd
print("This is the top 10 of the error request: ")
for k, v in Counter(error_domains).most_common(10):
    print(k, v)

print("This is the number of the lines in the log: ",line_count)
print("This is the number of the success request: ",request_success_count)
print("This is the number of the error request: ",request_error_count)


