import random

def get_reflector_list():
    """
    リフレクタを一つランダムに取得する。
    """
    normal_list = [chr(i) for i in range(65, 65+26)]
    result_list = [['',''] for i in range(65, 65+13)]

    r1 = random.randrange(13)
    r2 = random.randrange(2)

    for i in range(26):
        while(result_list[r1][r2] != ''):
            r1 = random.randrange(13)
            r2 = random.randrange(2)

        result_list[r1][r2] = normal_list[i]

    return result_list


def reflector_encrypt(plain_text, reflector):
    """暗号処理"""
    cryptgram = ''
    try:
        for i in range(len(plain_text)):
            for j in range (13):
                for k in range(2):
                    if plain_text[i] in reflector[j][k]:
                        if k==1:
                            cryptgram += reflector[j][0]
                        else :
                            cryptgram += reflector[j][1]

    except IndexError:
        print("PLAINTEXTMUSTBECAPITAL")

    #print("reflecter :" + plain_text)
    #print("reflecter :" +cryptgram)
    return cryptgram


def reflector_decrypt(cryptgram, reflector):
    """復号処理"""
    plain_text = ''
    try:
        for i in range(len(cryptgram)):
            for j in range (13):
                for k in range(2):
                    if plain_text[i] in reflector[j][k]:
                        if k==1:
                            cryptgram += reflector[j][0]
                        else :
                            cryptgram += reflector[j][1]

    except IndexError:
        print("CRYPTGRAMMUSTBECAPITAL")

    print("reflector :" +cryptgram)
    print("reflector :" +plain_text)
    return plain_text
