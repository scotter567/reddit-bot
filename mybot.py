import praw
import config
import os

def bot_login():
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "/u/Statellyfall's First Bot")

    return r

def run_bot(r, p_submission, temp):
    for submission in r.subreddit('hiphopheads').hot(limit=10):
        if '[FRESH]' in submission.title:
            temp.append(submission)
            submission_title.append(submission.title)
            submission_title.append('https://www.reddit.com/r/hiphopheads/' + submission.id)

    return  submission_title, temp

submission_title = []
r = bot_login()
temp = []

submission_title, temp = run_bot(r, submission_title, temp)

x = len (submission_title)
y = len (temp)

input_file = open('workfile.txt', 'w')

for i in range(0,x,2):
    z = int(i/2)
    input_file.write(str (temp[z])+'\n')
    #print (temp[z])
    input_file.write(submission_title[i]+'\n')
    input_file.write("URL: " + submission_title[i+1]+'\n')
    #print submission_title[i] + "\nURL: " + submission_title[i+1]

input_file = open('workfile.txt', 'r')

hey = "hey"
for line in input_file:
    hey = line
    print (line)

print ("0")
print (hey)
print ("0")