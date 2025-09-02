import sys

while True:
    try:
        data=input()
        print(data)
    except EOFError:
        break