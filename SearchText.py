#Find the specific word in a paragraph

fh = open('/Users/dushmantakumar/Qbot/q_bot/cont_matching/base_files/file1.txt','r')
word = input ("Enter the word to search:")
s = " "
count = 1
while(s):
    s = fh.readline()
    L = s.split()
    if word in L:
        print("Line number",count,":",s)

    count+=1