#!/usr/bin/python3
print(*[chr(65 + i) if i % 2 == 0 else chr(97 + i) for i in range(52, -1, -1)][::-1])
