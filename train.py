from collections import Counter
from features import *
import  os.path
import sys
emails_data = {"body":"", "sig":0, "attach":0, "count":0}
#python debugger
#import pdb
#db.set_trace()
#user input directory name containing files of training (mails)
directory = input("Directory: ")
#user inputs the output file names where we will print stemmed filtered words of mails with their numbers
output_name = input("Output: ")
#loop over all files in directory
for root, _, files in os.walk(directory):
    for file_obj in files:
        file_name = os.path.join(root, file_obj)
        #next two lines print a '.' on reading each file to show progress
        sys.stdout.write(".")
        sys.stdout.flush()
        #open each file in directory and read them
        with open(file_name, errors="replace") as f:
            mail = f.read()
        emails_data["count"] += 1
        props = email_parser(mail)
        if "sig" in props.keys():
            emails_data["sig"] += 1
        if "attach" in props.keys():
            emails_data["attach"] += 1
        if "body" in props.keys():
            emails_data["body"] += " " + lemmatize_string(props["body"])
        
s = set(emails_data["body"].split(" "))
c = Counter()
c["SIG"] = emails_data["sig"]
c["ATT"] = emails_data["attach"]
c["COUNT"] = emails_data["count"]
for word in emails_data["body"].split(" "):
    c[word] += 1
print ("\n Unique Words: " + str(len(s)))
with open(output_name + ".py", "w") as o:
    o.write("from collections import Counter\n" + output_name + " = ")
    o.write(str(c))
    o.close()