def simplifyPath(path: str) -> str:
    path = path.split('/')
    arr = []

    for char in path:

        if len(char) == 0 or char == '.':
            continue
        elif char == '..':
            if len(arr) > 0:
                arr.pop()
        else:
            arr.append(char)

    return '/' + '/'.join(arr)


for value in ["/home/","/../","/home//foo/","/a/./b/../../c/"]:
    print(simplifyPath(value))