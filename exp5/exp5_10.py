def valid_ip(s):
    n = len(s)
    for i in range(1,4):
        for j in range(i+1, i+4):
            for k in range(j+1, j+4):
                if k < n:
                    p1 = s[:i]
                    p2 = s[i:j]
                    p3 = s[j:k]
                    p4 = s[k:]
                    parts = [p1,p2,p3,p4]
                    if all(str(int(p)) == p and 0 <= int(p) <= 255 for p in parts):
                        print(".".join(parts))

valid_ip("25525511135")