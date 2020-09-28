# Imma try using recursion for this
glob = [1,2,3,4,5]
box = []

def reverse_array(glob: list):
    if len(glob) > 0:
        box.append(glob[-1])
        glob.pop()
        reverse_array(glob)


reverse_array(glob)
print(glob)
print(box)