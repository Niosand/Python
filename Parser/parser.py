from parser_module import get_txt, print_html, print_result, get_title, get_content


for i in range(5):
    txt = get_txt(i+1)
    title = get_title(txt)
    lst = (str(i+1) + ' ' + title)
    print(lst)
a = int(input('Введите номер канала - '))
txt = get_txt(a)
title = get_title(txt)
lines = get_content(txt)

result = title + '\n' + '\n'.join(lines)

print(result)  # это для контроля
print_result('result.txt', result)

