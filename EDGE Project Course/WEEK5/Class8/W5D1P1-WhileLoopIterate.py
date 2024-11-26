

name="sazib"

s=iter(name)

while True:
    try:
        c=next(s)
        print(c)
    except StopIteration:
        break
        