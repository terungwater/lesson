"""
Implement slug_maker(title). 
Remove leading and trailing spaces, convert the text to lowercase, 
remove commas and periods, and replace spaces with hyphens. 
Return the final slug.
"""

def slug_maker(title):
    title = title.strip()
    title = title.replace(",", "").replace(".", "")
    title = title.lower()
    i = 0
    while i < len(title):
        char = title[i]
        if char == " ":
            title = title.replace(" ", "-")
        i += 1
    return title
print(slug_maker(" ,hello, world. "))