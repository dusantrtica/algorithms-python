# to match prefix of the pattern with the suffix of the text
def build_prefix_suffix_table(pattern):
    m = len(pattern)
    lps = [0 for _ in range(m)]
    j = 1
    i = 0
    lps[0] = 0
    while j < m:
        if pattern[i] == pattern[j]:
            lps[j] = i + 1
            j += 1
            i += 1
        else:
            if i != 0:
                i = lps[i-1]
            else:
                lps[j] = 0
                j += 1
    return lps


def kmp(s, t):
    n = len(s)
    m = len(t)
    lps_table = build_prefix_suffix_table(t)
    i = 0
    j = 0
    while i < n:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            if j > 0:
                j = lps_table[j - 1]
            else:
                i += 1
        if j == m:
            return True

    return False


def test_partial_table():
    assert build_prefix_suffix_table("onions") == [0, 0, 0, 1, 2, 0]
    assert build_prefix_suffix_table("trains") == [0, 0, 0, 0, 0, 0]
    assert build_prefix_suffix_table("ttta") == [0, 1, 2, 0]
    assert build_prefix_suffix_table("aabaaac") == [0, 1, 0, 1, 2, 2, 0]


def test_kmp():
    assert kmp("onionionspl", "onions") is True
    assert kmp("dusan", "sa") is True
    assert kmp("dusan", "uss") is False
