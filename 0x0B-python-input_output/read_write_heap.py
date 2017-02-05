#!/usr/bin/python3
import ctypes
"""
this is module read_write_heap
modify the heap of a process
"""


def read_maps(pid):
    print("[*] Maps: /proc/{}/Maps".format(pid))
    with open("/proc/{}/maps".format(pid), mode="r", encoding="utf-8") as f:
        for line in f:
            if "[heap]" in line:
                heap_found = True
                print(line)
                break
    line_split = line.split()
    if heap_found:
        print("[*] Found [heap]:")
        print("    pathname = {}".format(line_split[-1]))
        print("    addresses = {}".format(line_split[0]))
        print("    permissions = {}".format(line_split[1]))
        print("    offset = {}".format(line_split[2]))
        print("    inode = {}".format(line_split[-2]))
        addr = line_split[0].split("-")
        print("[*] Addr start [{}] | end [{}]".format(addr[0], addr[1]))
        for address in range(int(addr[0], 16), int(addr[1], 16)):
            res = ctypes.c_char_p(address)
            print(type(res.value))



read_maps(11195)
