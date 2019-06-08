import binascii
import os
import time

start = time.time_ns()
def seperatefiles(start,end,folder = "files/"):
    png = "89504e470d0a1a0a"
    jpg = "ffd8ffe0"
    mp3 = "494433"

    os.mkdir("jpg")
    os.mkdir("png")
    os.mkdir("mp3")
    os.mkdir("txt")


    for x in range(start,end):
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

seperatefiles(1,150)
end = time.time_ns()
print("Time is: " + str(end - start) + " nanosecond for single threading...")