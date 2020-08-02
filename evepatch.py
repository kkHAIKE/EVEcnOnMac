import sys
import os
import re
import hashlib

def patch(fpath):
    with open(fpath, "rb") as f:
        data = f.read()

    cnt = 0
    # mov rax, gs:60h
    for m in re.finditer(r"\x65\x48\x8b\x04\x25\x60\x00\x00\x00", data):
        s = m.start()
        e = m.end()
        if data[e + 2: e + 6] == "\xbc\x00\x00\x00":
            c = 0x15
        else:
            r = re.search(r"\x7c......\xe8", data[e:])
            c = r.start() + 9

        print "patch", hex(s), hex(c)
        data = data[:s] + "\xeb" + chr(c) + "\x90"*7 + data[e:]

        cnt += 1

    assert cnt == 3 or cnt == 0

    if cnt == 3:
        with open(fpath, "wb") as f:
            f.write(data)

        return hashlib.md5(data).hexdigest()

    return None

def changeHash(fpath, h):
    with open(fpath, "rt") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if not line.startswith("app:/EVEGuardx64.exe,"):
            continue

        arr = line.split(",")
        arr[2] = h
        lines[i] = ",".join(arr)

        with open(fpath, "wt") as f:
            f.writelines(lines)

        print "changeHash", h
        break

def main(argv):
    if len(argv) <= 1:
        print "python evepatch.py EVEdir"
        return

    guardx64 = os.path.join(argv[1], "SharedCache", "serenity", "EVEGuardx64.exe")
    index = os.path.join(argv[1], "SharedCache", "index_serenity.txt")
    assert os.path.exists(guardx64) and os.path.exists(index)

    h = patch(guardx64)
    if h is not None:
        changeHash(index, h)

    print "ok"

main(sys.argv)
