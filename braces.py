class Stack():
    def __init__(self):
        self.main_stack = []

    def isEmpty(self):
        if self.main_stack == []:
            return True
        else:
            return False

    def push(self, new_element):
        self.main_stack.insert(0, new_element)
        pass

    def pop(self):
        if self.isEmpty() is False:
            return self.main_stack.pop(0)
        else:
            return False

    def peek(self):
        if self.isEmpty() is False:
            return self.main_stack[0]
        else:
            return False

    def size(self):
        return len(self.main_stack)

    def show(self):
        return self.main_stack


def check(str):
    # Следующих конструкций не должно быть в строке, если есть сразу False.
    if '(]' in str or '[)' in str or '[}' in str or '{]' in str or '(}' in str or '{)' in str:
        return 'Несбалансированно'
    # Далее работаем со списком
    get_list = list(str)
    # Создаем экземпляры стеков которые будем заполнять и освобождать
    # Для скобок {}
    braces = Stack()
    # Для скобок ()
    parentheses = Stack()
    # Для скобок []
    square_brackets = Stack()

    # Проходим по списку
    for element in get_list:
        # print(parentheses.show())
        # добавляем если скобка открыта
        if element == '(':
            parentheses.push(element)
        # удаляем если скобка закрыта
        elif element == ')':
            # Если в стеке нечего удалять значит закрытых больше и это уже не корректно возвращаем False
            if parentheses.peek() is False:
                return 'Несбалансированно'
            # удаляем если скобка закрыта
            else:
                parentheses.pop()

        # Далее аналогично
        elif element == '[':
            square_brackets.push(element)
        elif element == ']':
            if square_brackets.peek() is False:
                return 'Несбалансированно'
            else:
                square_brackets.pop()

        elif element == '{':
            braces.push(element)
        elif element == '}':
            if braces.peek() is False:
                return 'Несбалансированно'
            else:
                braces.pop()

    # Если стеки после перебора пусты значит все корректно
    if parentheses.size() == 0 and square_brackets.size() == 0 and braces.size() == 0:
        return 'Сбалансированно'
    else:
        return False


if __name__ == '__main__':
    # сбалансированны  последовательности:
    a = '(((([{}]))))'
    b = '[([])((([[[]]])))]'
    c = '{()}'
    d = '{{[()]}}'
    # Несбалансированные последовательности:
    e = '}{}'
    f = '{{[(])]}}'
    g = '[[{())}]'

    # Проверяем
    print(f'a - {check(a)}')
    print(f'b - {check(b)}')
    print(f'c - {check(c)}')
    print(f'd - {check(d)}')
    print(f'e - {check(e)}')
    print(f'f - {check(f)}')
    print(f'g - {check(g)}')

