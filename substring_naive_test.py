def substr(s, t):
    n = len(s)
    m = len(t)

    i = 0
    while i < n - m + 1:
        j = 0

        while j < m:
            if s[i + j] != t[j]:
                break
            j += 1
        if j == m:
            return True
        i += 1
    return False


def test_substr():
    assert substr("tttta", "ta") is True
    assert substr("dusan", "sa") is True
    assert substr("dusan", "st") is False
    assert substr("this is a test", "test") is True
