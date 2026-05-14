name = "SINEM SEN"
i = 0

while i < len(name):
    i += 1
    # COBOL indexing is 1-based, so we subtract 1 for Python's 0-based indexing
    print(name[i - 1])
