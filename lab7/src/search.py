def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(haystack, needle):
    if not needle:
        return []

    lps = compute_lps(needle)
    result = []

    i = 0
    j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result


with open('lab7/input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    haystack = lines[0].strip()
    needle = lines[1].strip()

indices = kmp_search(haystack, needle)

with open('lab7/output.txt', 'w', encoding='utf-8') as f:
    f.write(" ".join(map(str, indices)))
