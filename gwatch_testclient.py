#!/usr/bin/python3

from gi.repository import GObject, GLib
import os
import gwatch_lib


def my_read_cb(value):
    print('my callback: {}'.format(value))


def my_write_cb(my_server):
    cpu_temp = os.popen('df -h').readline()
    if my_server.fd_available():
        my_server.write_spp('{}'.format(cpu_temp))
        print('Sending: {}'.format(cpu_temp))
    return True


if __name__ == '__main__':
    my_spp_server = gwatch_lib.SPP(my_read_cb)
    GLib.timeout_add(1000, my_write_cb, my_spp_server)
    my_spp_server.start()
