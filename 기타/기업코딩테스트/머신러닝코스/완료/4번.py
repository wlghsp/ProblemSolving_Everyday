"""
Content of "log.txt":
10.1.2.1 - car [01/Mar/2022:13:05:05 +0900] "GET /python HTTP/1.0" 200 2222
10.1.1.9 - bike [01/Mar/2022:13:05:10 +0900] "GET /python HTTP/1.0" 200 2222

Expected output:
01/Mar/2022:13:05:05 +0900
01/Mar/2022:13:05:10 +0900
"""
def tail(filename, n=10):
    with open(filename, "r") as f:
    	lines = f.readlines()
    for line in lines[len(lines)-n:]:
        print(line)


tail("../file.txt")