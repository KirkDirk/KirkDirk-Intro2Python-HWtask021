# Напишите программу, удаляющую из текста 
# все слова, содержащие ""абв""

with open('D:\SASLearn\HW(python)\HWtask021\data.txt', 'r', encoding='utf-8') as data:
    some_text = data.read()

text_to_words = some_text.split(' ')
find_text = 'абв'
text_without = []
end_text = ''
for i in text_to_words:
    if find_text not in i:
        text_without.append(i)
for j in range(len(text_without)):
    end_text += text_without[j]+' '

with open('D:\SASLearn\HW(python)\HWtask021\esu.txt', 'w', encoding='utf-8') as resu:
    resu.write(end_text)