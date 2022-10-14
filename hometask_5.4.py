# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open ('file_5.4.txt', 'r') as data:
    text = data.readline()

# print(text)
def rle_coding(text):
    rle_text = ''
    count =1
    char = text[0]
    for i in range(1, len(text)):
        if text[i] == char:
            count +=1
        else:
            rle_text += str(count) + char
            char = text[i]
            count = 1
    rle_text += str(count) + char
    return rle_text

def rle_decoding(text):

    new_text = ''
    i = 0
    while len(text[i: i + 2]) == 2:
        num, char = text[i: i + 2]
        new_text += char * int(num)
        i += 2

    return new_text


coding_text = rle_coding(text)
# print(rle_codding(text))
decoding_text = rle_decoding(coding_text)
# print(rle_decooding(codding_text))

with open ('file_5.4_coding.txt', 'w', encoding = 'utf-8') as data:
    data.write(coding_text)
with open('file_5.4_decoding.txt', 'w', encoding = 'utf-8') as data:
    data.write(decoding_text)
