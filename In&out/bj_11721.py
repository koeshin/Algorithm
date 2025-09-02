import sys

words=sys.stdin.readline()

n=0
while(n<len(words)):
    start=n
    end=n+10
    
    if end> len(words):
        end=len(words)
    print(words[start:end])

    n=end