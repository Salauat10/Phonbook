main_menu = ['Главное меню',
            'Открыть телефонную книгу',
            'Сохранить телефонную книгу',
            'Показать контакт',
            'Создать контакт',
            'Найти контакт',
            'Изменить контакт',
            'Удалить контакт',
            'Выход']

choice_main_menu = f'Выберите пункт меню ({1} - {len(main_menu) - 1}):'
choice_main_menu_error = f'Нужно ввести число от 1 до {1} - {len(main_menu) - 1}!'

phone_book_opened_successful = 'Телефонная книга открыта успешно!'

phone_book_saved_successful = 'Телефонная книга сохранена успешно!'

phone_book_deleted_successful = 'Телефонная книга удалена успешно!'

empty_phone_book_error = 'Телефонная книга пуста или не открыта!'

input_new_contact = ['Введите имя контакта: ', 
                    'Введите номер контакта: ', 
                    'Введите коммент для контакта: ']

no_changes = 'или ENTER, чтобы оставить без изменений'

edit_contact = ['Введите новое имя ({no_changes}): ', 
                'Введите новый номер ({no_changes}): ', 
                'Введите новый комментарий ({no_changes}): ']

input_search_word = 'Введите слово для поиска: '
input_search_word_for_edit = 'Введите слово для поиска, который хотите изменить: '
input_search_word_for_delete = 'Введите слово для поиска, который хотите удалить: '
input_id_for_edit = 'Введите ID контакта, который хотите изменить: '
input_id_for_delete = 'Введите ID контакта, который хотите удалить: '


def new_contact_added_successfully(name: str) -> str:
    return f'Контакт "{name}" добавлен успешно!'

def find_contact_no_result(word: str) -> str:
    return f'Контакт с таким словом "{word}" не найден!'


def edit_contact_successful(name) -> str:
    return f'Контакт "{name}" изменен успешно!'


def delete_contact_successful(name) -> str:
    return f'Контакт "{name}" удален успешно!'


