def get_logs_lines(file, n=1, bs=1024):
    """
    Takes the log file as parameters.
    Returns the lines of the log file.
    """
    file_item = open(file)
    file_item.seek(0, 2)
    line = 1-file_item.read(1).count('\n')
    B = file_item.tell()
    while n >= line and B > 0:
            block = min(bs, B)
            B -= block
            file_item.seek(B, 0)
            line += file_item.read(block).count('\n')
    file_item.seek(B, 0)
    line = min(line, n)
    lines = file_item.readlines()[-line:]
    file_item.close()
    return lines
