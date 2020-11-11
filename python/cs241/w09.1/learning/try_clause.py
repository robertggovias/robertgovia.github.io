import sys

try:
    f = open('integer.txt')
    s = f.readline()
    i = int(s.strip())
except (IOError, ValueError):
    print("An IO error or a ValueError occurred")
except:
    print ("An unexpected error occurred")
    raise