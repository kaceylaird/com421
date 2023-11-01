keys = [36, 88, 54, 28, 49, 21, 63, 7, 19, 2, 11, 41, 34]
hash_codes = [(2 * key + 3) % 17 for key in keys]
print(hash_codes)