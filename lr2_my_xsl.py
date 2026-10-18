import xml.dom.minidom as minidom


def open_table():
    try:
        with open('currency.xml', 'r', encoding='cp1251') as xml_file:
            dom = minidom.parse(xml_file)
        dom.normalize()
        return dom
    except FileNotFoundError:
        print('Файл не найден!')
        return 0



if __name__ == '__main__':
    dom = open_table()
    if dom == 0:
        exit()
    val_dict = {}
    for node in dom.getElementsByTagName('Valute'): # находим узлы с тегом book
        NumCode = CharCode = None
        for child in node.childNodes: # все дочерние узлы 
            if child.nodeType != 1: # не элемент пропукаем
                continue
            if child.firstChild is None or child.firstChild.nodeType != 3:
                # без текста пропускаем
                continue
            if child.tagName == 'NumCode': # проверяем тэг
                NumCode = child.firstChild.data.strip()
            elif child.tagName == 'CharCode':
                CharCode = child.firstChild.data.strip()
        val_dict[NumCode] = CharCode
    for num, char in val_dict.items():
        print(num, char)

