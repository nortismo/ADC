from vnc_eds import vncEds
import time


def main():
    vnc_eds = vncEds.VncEDS()
    while True:
        vnc_eds.update()
        time.sleep(1)


if __name__ == '__main__':
    main()
