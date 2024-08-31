def ords(text,delimiter = ","):
    newtext = []
    for t in text:
        newtext.append(str(ord(t)))
    return delimiter.join(newtext)


def chrs(text,delimiter = ","):
    newtext = []
    words = text.split(delimiter)
    for w in words:
        newtext.append(str(chr(w)))
    return "".join(newtext)
