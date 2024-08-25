def SortFileLinesByKey(file_path, file_path2, function):
    """
    Sorts the lines of a file by the key at the given index.
    The key is the part of the line that is separated by the separator.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines.sort(key=function)
    
    # write to file
    with open(file_path2, 'w') as file:
        for line in lines:
            file.write(line)


def key(line):
    try:
        return 1e9 - int(line.removeprefix('elapsed: ').split(',')[0])
    except Exception:
        return 1e9 + 1


if __name__ == "__main__":
    SortFileLinesByKey('debug2.txt', 'debugpolicy.txt', key)
