import sys

def progress_bar(cur, total, end=False):
    progress = cur * 100 // total
    sys.stdout.write("\r[%-100s] %d%%" % ('=' * progress, progress))


from time import sleep
if __name__ == "__main__":
    total = 30
    for i in range(total):
        sleep(0.1)
        progress_bar(i, total)
    progress_bar(total, total)