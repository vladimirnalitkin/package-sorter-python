import sys
from package_sorter import sort


def main():
    if len(sys.argv) != 5:
        print("Usage: python main.py <width> <height> <length> <mass>")
        sys.exit(1)

    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
        length = int(sys.argv[3])
        mass = int(sys.argv[4])

        print(sort(width, height, length, mass))
    except ValueError as e:
        print(str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
