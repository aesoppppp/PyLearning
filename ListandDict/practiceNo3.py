phone_book = {}


def input_mode():
    while True:
        name = input('(입력모드) 이름을 입력하시오: ')
        if not name:
            search_mode()
            break
        elif name == 'exit':
            exit()
        tel = input('전화번호를 입력하시오: ')
        phone_book[name] = tel


def search_mode():
    while True:
        search_name = input('(검색모드) 이름을 입력하시오: ')
        if not search_name:
            input_mode()
            break
        elif search_name == 'exit':
            exit()
        print(f'{search_name}의 전화번호는 {phone_book[search_name]} 입니다.')


input_mode()
