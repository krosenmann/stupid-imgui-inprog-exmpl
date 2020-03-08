#!/usr/bin/env python3
import importlib
import os

import main
import main_frame


def main_frame_mod_time():
    return int(os.path.getmtime(main_frame.__file__))


def amain():
    last_mod_time = main_frame_mod_time()
    args = main_frame.init()
    while True:
        if last_mod_time < main_frame_mod_time():
            last_mod_time = main_frame_mod_time()
            importlib.reload(main_frame)
            args = main_frame.init()
        main.draw(*args)
        importlib.reload(main)


if __name__ == '__main__':
    amain()
