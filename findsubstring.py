def find_substr(string, substring):
    for i in range(len(string) - len(substring) + 1):
        found = True
        for j in range(len(substring)):
            if string[i + j] != substring[j]:
                found = False
                break
        if found:
            return i
    return -1


res = find_substr('arpine', 'arpi')
if res != -1:
    print(f"Substring found at index {res}")
else:
    print("Substring not found")
