# Напишите программу, удаляющую из текста 
# все слова, содержащие ""абв""

def get_word_pos(t, x):
    x_0 = x_end = x
    while x_0 != ' ' or x_0 >= t[0]:
        x_0 -= 1
    while x_end != ' ' or x_end <= t[-1]:
        x_end += 1
    return [x_0, x_end]

some_text = """жфдол лофа фло лодавб фалоф авв 
    фвалва лабввы ыдлаф абв фаф лодфтмфтд"""

# while some_text.find('абв') != -1:
#     get_word_pos(some_text, some_text.find('абв'))

text_to_words = some_text.split(' ')
find_text = 'абв'
text_without = []
end_text = ''
for i in text_to_words:
    if find_text not in i:
        text_without.append(i)
for j in range(len(text_without)):
    end_text += text_without[j]+' '
print(end_text)