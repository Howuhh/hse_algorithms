
 def z_function(s):
    ...:     z = [0] * len(s)
    ...:     l, r = 0, 0
    ...:     for i in range(1, len(s)):
    ...:         k = max(min(z[i - l], r - i), 0)
    ...:         while i + k < len(s) and s[k] == s[i + k]:
    ...:             k = k + 1
    ...:         z[i] = k
    ...:         if i + z[i] > r:
    ...:             l, r = i, i + z[i]
    ...:     return z


 def prefix_function(s):
    ...:     pi = [0] * len(s)
    ...:     for i in range(1, len(s)):
    ...:         k = pi[i - 1]
    ...:         while k > 0 and s[i] != s[k]:
    ...:             k = pi[k - 1]
    ...:         if s[i] == s[k]:
    ...:             pi[i] = k + 1
    ...:     return pi