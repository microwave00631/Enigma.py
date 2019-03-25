
import rotor
import reflector
import plagboard

ROTOR1 = rotor.get_rotor_list()
ROTOR2 = rotor.get_rotor_list()
ROTOR3 = rotor.get_rotor_list()
REFLECTOR = reflector.get_reflector_list()
PLAGBOARD = plagboard.get_plagboard_list(5)


ROTOR_DICT = {"ROTOR1" : ROTOR1, "ROTOR2" : ROTOR2,"ROTOR3" : ROTOR3}

plagboard_const = [['B', 'I'], ['G', 'J'], ['F', 'D'], ['A', 'L'], ['E', 'H']]

rotor1_const = (('A', 'B'), ('B', 'P'), ('C', 'G'), ('D', 'E'), ('E', 'J'), ('F', 'V'), ('G', 'K'), ('H', 'Z'),('I', 'S'),\
                ('J', 'W'), ('K', 'M'), ('L', 'O'), ('M', 'X'), ('N', 'R'), ('O', 'I'), ('P', 'T'),('Q', 'C'), ('R', 'F'),\
                ('S', 'Q'), ('T', 'Y'), ('U', 'D'), ('V', 'U'), ('W', 'H'), ('X', 'A'), ('Y', 'N'), ('Z', 'L'))
rotor2_const = (('A', 'E'), ('B', 'Y'), ('C', 'F'), ('D', 'A'), ('E', 'X'), ('F', 'G'), ('G', 'I'), ('H', 'W'), ('I', 'Q'),\
                ('J', 'C'), ('K', 'T'), ('L', 'R'), ('M', 'N'), ('N', 'M'), ('O', 'S'), ('P', 'L'), ('Q', 'K'), ('R', 'V'),\
                ('S', 'B'), ('T', 'J'), ('U', 'H'), ('V', 'P'), ('W', 'O'), ('X', 'U'), ('Y', 'Z'), ('Z', 'D'))
rotor3_const = (('A', 'B'), ('B', 'K'), ('C', 'S'), ('D', 'G'), ('E', 'M'), ('F', 'Y'), ('G', 'N'), ('H', 'J'), ('I', 'C'),\
                ('J', 'I'), ('K', 'E'), ('L', 'U'), ('M', 'Q'), ('N', 'V'), ('O', 'W'), ('P', 'A'), ('Q', 'F'), ('R', 'O'),\
                ('S', 'L'), ('T', 'Z'), ('U', 'R'), ('V', 'T'), ('W', 'P'), ('X', 'D'), ('Y', 'H'), ('Z', 'X'))

reflector_const = [['O', 'N'], ['S', 'V'], ['W', 'K'], ['U', 'I'], ['J', 'R'], ['C', 'E'], ['X', 'G'],\
                     ['D', 'Z'], ['L', 'Y'], ['A', 'Q'], ['H', 'P'], ['M', 'T'], ['F', 'B']]

#print(ROTOR1)
#print(ROTOR2)
#print(ROTOR3)

#print("choose key")

#FIRST_KEY = input('choose first rotor \n >> ')
#SECOND_KEY = input('choose second rotor \n >> ')
#THIRD_KEY = input('choose third rotor \n >> ')


def encrypt(plain_text, rotor1, rotor2, rotor3, reflector_name,*plagboard_name): 
    cryptgram = ''

    #タプルからリストへの変換
    rotor1_actual = tuptle_to_list(rotor1)
    rotor2_actual = tuptle_to_list(rotor2)
    rotor3_actual = tuptle_to_list(rotor3)
    
    #プラグボードを刺す
    if plagboard_name != None :
        plain_text = plagboard.connect_code(plain_text,plagboard_name[0])

    for i in range(len(plain_text)):
        # 三つのロータを通す
        encrypt1 = rotor.rotor_encrypt(plain_text[i],rotor1_actual)
        encrypt2 = rotor.rotor_encrypt(encrypt1,rotor2_actual) 
        encrypt3 = rotor.rotor_encrypt(encrypt2,rotor3_actual) 

        #リフレクターを通す
        reflect = reflector.reflector_encrypt(encrypt3,reflector_name)

        #三つのロータをさらに逆から通す
        decrypt1 = rotor.rotor_decrypt(reflect, rotor3_actual)
        decrypt2 = rotor.rotor_decrypt(decrypt1,rotor2_actual)
        decrypt3 = rotor.rotor_decrypt(decrypt2,rotor1_actual)

        cryptgram += decrypt3
        #ロータをまわす
        rotor1_actual = rotor.pivot_rotor(rotor1_actual)
        if(i%26 == 0 and i != 0):
            rotor2_actual = rotor.pivot_rotor(rotor2_actual)
        if(i%(26**2) == 0 and i != 0):
            rotor3_actual = rotor.pivot_rotor(rotor3_actual)
    
    #プラグボードを刺す
    if plagboard_name != None :
        cryptgram = plagboard.connect_code(cryptgram,plagboard_name[0])

    print( "encrypted : " + cryptgram )

    return cryptgram
    
def decrypt(cryptgram, rotor1, rotor2, rotor3, reflector_name, *plagboard_name):
    plain_text = ''

    #タプルからリストへの変換
    rotor1_actual = tuptle_to_list(rotor1)
    rotor2_actual = tuptle_to_list(rotor2)
    rotor3_actual = tuptle_to_list(rotor3)
    
    #プラグボードを刺す
    if plagboard_name != None :
        cryptgram = plagboard.connect_code(cryptgram,plagboard_name[0])

    for i in range(len(cryptgram)):

        # 三つのロータを通す
        encrypt1 = rotor.rotor_encrypt(cryptgram[i],rotor1_actual) 
        encrypt2 = rotor.rotor_encrypt(encrypt1,rotor2_actual) 
        encrypt3 = rotor.rotor_encrypt(encrypt2,rotor3_actual) 

        #リフレクターを通す
        reflect = reflector.reflector_encrypt(encrypt3, reflector_name)

        #三つのロータをさらに逆から通す
        decrypt1 = rotor.rotor_decrypt(reflect, rotor3_actual)
        decrypt2 = rotor.rotor_decrypt(decrypt1,rotor2_actual)
        decrypt3 = rotor.rotor_decrypt(decrypt2,rotor1_actual)

        plain_text += decrypt3

        #ロータをまわす
        rotor1_actual = rotor.pivot_rotor(rotor1_actual)
        if(i%26 == 0 and i != 0):
            rotor2_actual = rotor.pivot_rotor(rotor2_actual)
        if(i%(26**2) == 0 and i != 0):
            rotor3_actual = rotor.pivot_rotor(rotor3_actual)

    #プラグボードを刺す
    if plagboard_name != None :
        plain_text = plagboard.connect_code(plain_text,plagboard_name[0])

    print( "decrypted : " + plain_text )

    return plain_text


def tuptle_to_list(tuple_input):
    result = []

    for i in range(len(tuple_input)):
        result.append(list(tuple_input[i]))

    return result


if __name__ == '__main__':

    cr = encrypt("THISNULLISNULLTESTNULLMESSAGENULLYOUNULLCANNULLRECEIEVENULLTHISNULLMESSAGENULLWITHOUTNULLWIRETAP", rotor1_const, rotor2_const, rotor3_const, reflector_const,plagboard_const)

    de = decrypt(cr, rotor1_const, rotor2_const, rotor3_const, reflector_const, plagboard_const)

    decrypt(encrypt("THISNULLISNULLTESTNULLMESSAGENULLYOUNULLCANNULLRECEIEVENULLTHISNULLMESSAGENULLWITHOUTNULLWIRETAP",ROTOR1,ROTOR2,ROTOR3,REFLECTOR,PLAGBOARD),ROTOR1,ROTOR2,ROTOR3,REFLECTOR,PLAGBOARD)
