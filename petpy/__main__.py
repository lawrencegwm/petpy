import sys

from .petpy import gardner


def main():
    vp = float(sys.argv[1])
    print(gardner(vp))
    return


if __name__ == "__main__":
    main()