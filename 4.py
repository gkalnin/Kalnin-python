# Ответ: Данная последовательность [((())()(())]] не является правильной.
# Для того, чтобы сделать её правильной необходимо удалить крайнюю правую
# квардратную скобку и первую круглую скобку. Последовательность будет иметь вид [(())()(())].
# Ниже приведена функция для определения правильной последовательности.

def validate(x=str):
    '''The function returns True if bracket sequence is balanced. Returns False otherwise.'''
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    is_valid = True
    for el in x:
        if el in '([{':
            stack.append(el)
        elif el in ')]}':
            if not stack:
                is_valid = False
                break
            last = stack.pop()
            if last == pairs[el]:
                continue
            is_valid = False
            break
        else:
            return 'The function takes only a string consisted of parentheses, square brackets, and curly braces'
    return is_valid and len(stack) == 0

print('Введите скобочную последовательность: ')
test = input()
print(validate(test))