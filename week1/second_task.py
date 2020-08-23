def calculate(data, findall):
    matches = findall(r"([abc])([+-]?)=([abc]?)([+-]?[1-9]?[0-9]*)")
    for v1, s, v2, n in matches:
        if s == '':
            data[v1] = data.get(v2, 0) + int(n or 0)
        elif s == '+':
            print(data.get(v2, 0) + int(n or 0))
            data[v1] += data.get(v2, 0) + int(n or 0)
        else:
            data[v1] -= data.get(v2, 0) + int(n or 0)
    return data
