# name = input("Enter a name")
# name = name.strip().title()


tags = "hello, hi, nye"
tags = tags.split(",")
filtered =[tag.strip() for tag in tags]
final_tags = " | ".join(filtered)
print(final_tags)

def is_valid_email(e):
    i = e.find("@")
    if i != -1:
        j = e.find('.',i)
    if j >= 0:
        return True
    return False

print(is_valid_email("hello@gmail.com"))

def cipher(text):
    new = []
    for i in text:
        x = ord(i)
        if x == 122:
            x = 96
        new.append(chr(x+1))
    return "".join(new)

print(cipher("zzz"))


def slug(text):
    text = list(text)
    for i, char in enumerate(text):
        if char.isspace():
            text[i]="-"
        elif not char.isalnum():
            del text[i]
        print(text)
    return "".join(text)

print(slug("hello-78//"))