def rabin_karp(text, pattern):
    # prime number for modulo operator
    q = 31

    d = 26

    m = len(pattern)
    n = len(text)
    # hashes for the region of text and pattern
    hash_text = 0
    hash_pattern = 0

    # largerst polynomial
    h = 1

    for _ in range(m - 1):
        h = (h * d) % q

    # pre compute the hash of the pattern
    for i in range(m):
        hash_pattern = ((d * hash_pattern) + ord(pattern[i])) % q
        hash_text = (d * hash_text + ord(text[i])) % q

    # slide  the patern over text one by one
    for i in range(n - m + 1):
        if hash_text == hash_pattern:
            j = 0
            while j < m:
                if text[i + j] != pattern[j]:
                    break
                j = j + 1
            if j == m:
                return True

        # update the hash for the actual substring of the text
        if i < n - m:
            hash_text = ((hash_text - ord(text[i]) * h) * d + ord(text[i + m])) % q

            # we might get negative value so we have to make sure the hash is positive.
            if hash_text < 0:
                hash_text = hash_text + q
    return False


def test_rabin_karp():
    assert rabin_karp("dusan", "sa") is True
    assert rabin_karp("dusan", "st") is False
    assert rabin_karp("ttttttta", "tta") is True
