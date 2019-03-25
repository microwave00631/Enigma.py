import random

def get_plagboard_list(plag_number):
    """
    プラグボードを一つランダムに取得する。
    plag_numberには1から13の整数を入れる。
    """
    normal_list = [chr(i) for i in range(65, 65+26)]
    connect_list = [['',''] for i in range(65, 65 + plag_number)]

    r1 = random.randrange(plag_number)
    r2 = random.randrange(2)

    for i in range(plag_number*2):
        while(connect_list[r1][r2] != ''):
            r1 = random.randrange(plag_number)
            r2 = random.randrange(2)

        connect_list[r1][r2] = normal_list[i]

    return connect_list


def connect_code(plain_text,connect_list):
    result_text = ""
    for i in range(len(plain_text)):
        for j in range(len(connect_list)):

            if plain_text[i] in connect_list[j]:
                if plain_text[i] == connect_list[j][0]:
                    result_text += connect_list[j][1]
                else:
                    result_text += connect_list[j][0]

        if i == len(result_text):
            result_text += plain_text[i]

    return result_text
