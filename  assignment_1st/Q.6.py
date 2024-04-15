# write a code to perform basic string compresssion using the counts of repeated charactristics.
def compress_string(s):
    compressed = ""
    count = 1
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1
    return compressed if len(compressed) < len(s) else s

original_string = "aabbbccdddd"
compressed_string = compress_string(original_string)
print("Original string:", original_string)
print("Compressed string:", compressed_string)
