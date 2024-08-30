from pprint import pprint

def custom_write(file_name, strings):
    file_name = 'recording.txt'
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    for index, string in enumerate(strings):
        byte_position = file.tell()
        file.write(string + '\n')
        strings_positions[(index + 1, byte_position)] = string
        file.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('recording.txt', info)
for elem in result.items():
  print(elem)
