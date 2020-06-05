import aiml
import sys

response = "ciao url{myurl}  too url{sec}"
start = 0
text = ""
urls = ""
temp = 0
while temp >= 0:
    try:
        temp = response.index("url{", start)
        if temp >= 0:
            end = response.index("}", temp)
            urls = urls + response[temp+4:end] + " "
            text = text + response[start:temp]
            start = end+1
    except Exception as e:
        temp = -1
print(text)
sys.exit()


kernel = aiml.Kernel()
kernel.learn("startup.xml")
kernel.respond("load aiml b")
while 1:
    response = kernel.respond(input())
    print(response)
