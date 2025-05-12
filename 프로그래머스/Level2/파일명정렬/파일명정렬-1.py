def solution(files):
    repo = []
    for i, file in enumerate(files):
        head_number = split(file)
        repo.append((head_number[0], head_number[1], i))
    repo.sort(key=lambda x: (x[0], x[1], x[2]))
    return [files[r[2]] for r in repo]

def split(file):
    head = []
    for c in file:
        if c.isdigit():
            break
        head.append(c)
    number = []
    for c in file[len(head):]:
        if not c.isdigit():
            break
        number.append(c)
    return ''.join(head).lower(), int(''.join(number))

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]