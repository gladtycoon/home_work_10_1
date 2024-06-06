def mask_account_card(demask_number: list) -> list:
    """Маскирует номер счета или карты"""
    mask_number = ''
    count_digits = 0
    count_letters = 0
    count_spaces = 0
    for i in range(len(demask_number)):
        if demask_number[i].isalpha():
            mask_number += demask_number[i]
            count_letters += 1
        elif demask_number[i] == ' ':
            mask_number += ' '
            count_spaces += 1
        else:
            mask_number += demask_number[i]
            count_digits += 1
    if count_digits == 20:
        print(f'{mask_number[:5]}**{mask_number[-4:]}')
    elif count_digits != 20:
        if count_spaces > 2:
            print(f'{mask_number[:count_letters+1]} {mask_number[-19:-15]} **** **** {mask_number[-4:]}')
        else:
            print(f'{mask_number[:count_letters+1]} {mask_number[-16:-12]} **** **** {mask_number[-4:]}')

mask_account_card('Счет 35383033474447895560')
