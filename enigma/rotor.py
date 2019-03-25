"""This is a test program."""
import random

def get_rotor_list():
    """
    ローター盤を一つランダムに取得する。
    """
    normal_list = [chr(i) for i in range(65, 65+26)]
    tmp_list = ['' for i in range(65, 65+26)]

    result_list = [['', ''] for i in range(26) ]

    for i in range(26):
        if i == 0:
            e1 = _random_int(0, i, 25) #範囲内でランダムにイントを返す
            tmp_list[e1] = normal_list[i]
        else:
            while tmp_list[e1] != '':
                e1 = _random_int(0, i, 25)
            tmp_list[e1] = normal_list[i]
    
    if (tmp_list[25] == 'Z'):
        e2 = random.randrange(25)
        tmp_list[25] = tmp_list[e2]
        tmp_list[e2] = 'Z'

    #タプルのリストをつくる
    for i in range(65, 65+26):
        result_list[i-65] = ( chr(i), tmp_list[i-65])
    
    #タプルのリスト を タプルのタプル にする
    result_tuple = tuple(result_list)

    return result_tuple

def _random_int(start, slash, end):
    """start以上　slash未満,　slash 超過　end以下の整数をランダムに返す。 """
    if start == slash:
        return random.randrange(slash+1, end)
    elif slash == end:
        return end
    else:
        if random.choice([True, False]):
            return random.randrange(start, slash)
        else:
            if slash == end-1:
                return random.randrange(slash, end)
            else:
                return random.randrange(slash+1, end)


def rotor_encrypt(plain_text, rotor):
    """暗号処理"""
    cryptgram = ''
    try:
        for i in range(len(plain_text)):
            for j in range (26):
                    if plain_text[i] in rotor[j][0]:
                        cryptgram += rotor[j][1]
    except IndexError:
       print("PLAINTEXTMUSTBECAPITAL")
    #print(plain_text)
    #print(cryptgram)
    
    return cryptgram

def rotor_decrypt(cryptgram, rotor):
    """復号処理"""
    plain_text = ''
    try:
        for i in range(len(cryptgram)):
            for j in range (26):
                if cryptgram[i] in rotor[j][1]:
                    plain_text += rotor[j][0]
    except IndexError:
        print("CRYPTGRAMMUSTBECAPITAL")
    #print(cryptgram)
    #print(plain_text)

    return plain_text


def pivot_rotor(rotor):
    temp = rotor[0][1]
    for i in range(25):
        rotor[i][1] = rotor[i+1][1]
    rotor[25][1] = temp

    return rotor

