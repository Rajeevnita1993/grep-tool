import sys
import io
import os
import re

def grep(pattern, filename, invert_match):
    matched = False
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                found = re.search(pattern, line)
                if (found and not invert_match) or (not found and invert_match):
                    print(f"{filename}:{line}", end='')
                    #print(line, end='')
                    matched = True
    except UnicodeDecodeError:
        print(f"Skipping file due to encoding error: {filename}", file=sys.stderr)

    return matched

def grep_recursive(pattern, path, invert_match):
    matched = False
    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            if grep(pattern, filepath, invert_match):
                matched = True

    return matched


def main():
    if len(sys.argv) < 3:
        print("Usage: python my_grep.py [-r] [-v] <pattern> <file or directory>")
        sys.exit(1)

    # set the system output encoding to UTF-8
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    recursive = False
    invert_match = False
    case_insensitive = False
    arg_index = 1

    if sys.argv[arg_index] == "-r":
        recursive = True
        arg_index += 1

    if sys.argv[arg_index] == "-v":
        invert_match = True
        arg_index += 1

    if sys.argv[arg_index] == "-i":
        case_insensitive = True
        arg_index += 1

    pattern = sys.argv[arg_index]
    path = sys.argv[arg_index + 1]

    # convert search pattern to regular expression
    if case_insensitive:
        pattern = re.compile(pattern, re.IGNORECASE)
    else:
        pattern = re.compile(pattern)

    

    if recursive:
        matched = grep_recursive(pattern, path, invert_match)
    else:
        matched = grep(pattern, path, invert_match)

    if matched:
        sys.exit(0)
    else:
        sys.exit(2)

if __name__ == "__main__":
    main()