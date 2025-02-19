def rotation_cypher(word):
    result = ''
    for i in word:
        result += chr(ord(i) + 1).lower()
    return result

print(rotation_cypher("Attack"))