#!/usr/bin/python3
"""this module adds all arguments to a list then saves them to a file"""


def main():
    import sys
    import os.path
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    argv = sys.argv

    currentList = []
    args = argv
    args.remove(argv[0])
    if os.path.isfile("add_item.json") is True:
        currentList = load_from_json_file("add_item.json")
    save_to_json_file((currentList + args), "add_item.json")


if __name__ == "__main__":
    main()
