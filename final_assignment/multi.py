import binascii
import os
import time
import threading


start = time.time_ns()
def seperatefiles(first,last,folder = "files/"):
    png = "89504e470d0a1a0a"
    jpg = "ffd8ffe0"
    mp3 = "494433"

    os.mkdir("jpg")
    os.mkdir("png")
    os.mkdir("mp3")
    os.mkdir("txt")

    for x in range(first,last):
        file = "file" + str(x)
        with open(folder + file, "rb") as thisfile:
            header = thisfile.read(8)
            header = str(binascii.hexlify(header))[2:-1]
            if header.startswith(png):
                os.rename(folder + file, "png/" + file)
            elif header.startswith(jpg):
                os.rename(folder + file, "jpg/" + file)

            elif header.startswith(mp3):
                os.rename(folder + file, "mp3/" + file)
            else:
                os.rename(folder + file, "txt/" + file)



thread1 = threading.Thread(target = seperatefiles, args=(1, 51))
thread2 = threading.Thread(target = seperatefiles, args=(5, 101))
thread3 = threading.Thread(target = seperatefiles, args=(101, 150))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time_ns()

print("Time is: " + str(end- start) + " nanoseconds for multi threading")
