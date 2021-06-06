'''В этой модели главной является клавиша, которая имее: fine - штраф нажатии на нее, сколько раз была нажата данная клавиша. 
Надо переделпть, чтобы на одной клавише могло находится несколько букв.
'''
import collections


def get_keys_dict(text: str) -> dict:
    '''Считываем символы в тексте.'''
    return collections.Counter(text)

def get_text(file_name: str) -> str:
    '''Получаем текст.'''
    with open(file_name, encoding='utf-8') as file:
        return file.read()

TEXT = get_text('1grams-3.txt')
KEYS_DICT = get_keys_dict(TEXT.lower())
print(KEYS_DICT, len(KEYS_DICT.values()))


def divide_zero(func):
    def inner_func():
        pass
    return inner_func


class Key():
    def __init__(self, letters, fine, finger) -> None:
        ''' Это основной класс. Клавиша - это гланое в этой модели.

        В этом классе:
        letters - буквы, которые расположены на клавише. 
        fine - штраф, при нажатии на данную клавишу.
        presses - число нажатий на клавишу. Сумаа нажаний нажатий каждой буквы на клавише.
        finger - палец, который нажимает на данную клавишу.

        '''
        self.letters = letters
        self.fine = fine
        self.presses = 0
        self.finger = finger

        self.number_of_occurrences()
    
    def number_of_occurrences(self):
        '''На разные клавиши может нажимать один и тот же палец.

        Количество нажатий на клавишу равно сумме вхожений букв на этой клавише в текст.
        Нагрузка на палец равна сумме сколько раз он нажал на клавишу и штрафы при нажатии.

        '''
        for letter in self.letters:
            if letter in KEYS_DICT.keys():
                self.presses += KEYS_DICT[letter]
        
        self.finger.fine = self.presses * self.fine
        self.finger.stress += self.presses + self.finger.fine

        self.print_info_fine_and_loading()
        
    def print_info(self):
        print('------------------FINGER------------------')
        print('>>>Name: ', self.name)
        print('>>>Fine: ', self.fine)
        print('>>>Count: ', self.presses)
        print('>>>{} stress: '.format(self.finger.name), self.finger.stress)

    def print_info_fine_and_loading(self):
        print('На клавишу c {} нажал {} палец {} раз.'.format(self.letters, self.finger.name, self.presses))
        print('Штраф на него в данный момент {}'.format(self.finger.fine))
        print('--------------------------------------------------')

class Row():

    def __init__(self, name, keys) -> None:
        self.name = name
        self.keys = keys
        self.stress = 0

        self.set_stress()
    
    def print_info(self):
        print('---------{} ROW-------------'.format(self.name))
        for key in self.keys:
            for letter in key.letters:
                print('Буква \"{}\" ее печатали {} раз.'.format(letter, KEYS_DICT[letter]))
            print('На эту клавишу нажимали {} раз.'.format(key.presses))
            print('Штрафы на этот палец = {}'.format(key.finger.fine))
            print('Нагрузка на палец {} равна {}'.format(key.finger.name, key.finger.stress))
            print('---------------------------------------------------')

    def set_stress(self):
        '''
            Нагрузка на весь ряд - это сумма нагрузок на каждую клавишу в отдельности.
        '''
        for key in self.keys:
            self.stress += key.presses

    def stress_in_persent(self) -> str:
        if sum(KEYS_DICT.values()):
            return str(round(self.get_stress() / sum(KEYS_DICT.values()) * 100, 1)) + '%'
        else:
            return '0%'
    
    def get_stress(self):
        return self.stress

    def print_result(self):
        print('--------------------НАГРУЗКА НА {} РЯД-------------------'.format(self.name))
        print('Нагрузка на весь ряд равна: {}'.format(self.get_stress()))
        print('Нагрузка на весь ряд в процентах % равна: {}'.format(self.stress_in_persent()))


class Finger():
    def __init__(self, name) -> None:
        self.name = name
        self.stress = 0
        self.fine = 0


class Hand():
    '''
        У рук свое название.
    '''
    def __init__(self, name) -> None:
        self.name = name
        self.stress = 0
        self.fingers = {
            'fi2' : Finger('forefinger'), # Указательный палец
            'fi3' : Finger('middle_finger'),
            'fi4' : Finger('ring_finger'),
            'fi5' : Finger('little_finger'),
        }
    
    def set_stress(self):
        for finger in self.fingers.values():
            self.stress += finger.stress

    def get_stress(self):
        return self.stress 

    def print_result(self):
        self.set_stress()

        print('----------------НАГРУЗКА НА {} РУКУ-----------------'.format(self.name))
        print('Общая нагрузка на {} руку равна {} это сумма нагрузок на пальцы.'.format(self.name, self.get_stress()))
        for finger in self.fingers.values():
            print('Нагрузка на палец {} равна {}'.format(finger.name, finger.stress))
    

def main():
    left_hand = Hand('ЛЕВУЮ')
    right_hand = Hand('ПРАВУЮ')

    digital_row = Row('DIGITAL', [Key('ё', 5, left_hand.fingers['fi5']),# №41 left_hand
        Key(['1', '!'], 4, left_hand.fingers['fi5']), # №02
        Key('2', 4, left_hand.fingers['fi5']), # №03

        Key('3', 4, left_hand.fingers['fi4']), # №04

        Key('4', 4, left_hand.fingers['fi3']), # №05

        Key('5', 5, left_hand.fingers['fi2']), # №06
        Key(['6', ':'], 6, left_hand.fingers['fi2']), # №07 

        Key('7', 5, right_hand.fingers['fi2']), # 08 right_hand
        Key('8', 4, right_hand.fingers['fi2']), # 09

        Key(['9', '('], 4, right_hand.fingers['fi3']), # 10

        Key(['0', ')'], 4, right_hand.fingers['fi4']), # 11

        Key(['-', '_'], 4, right_hand.fingers['fi5']), # 12
        Key(['=', '+'], 5, right_hand.fingers['fi5']), # 13 
    ])

    home_row = Row('HOME', [Key('ф', 0, left_hand.fingers['fi5']),# №30 left_hand
        Key('ы', 0, left_hand.fingers['fi4']), # № 31
        Key('в', 0, left_hand.fingers['fi3']), # № 32

        Key('а', 0, left_hand.fingers['fi2']), # № 33
        Key('п', 0.5, left_hand.fingers['fi2']), # № 34left_hand

        Key('р', 0.5, right_hand.fingers['fi2']), # № 35right_hand
        Key('о', 0, right_hand.fingers['fi2']), # № 36

        Key('л', 0, right_hand.fingers['fi3']), # № 37
        Key('д', 0, right_hand.fingers['fi4']), # № 38

        Key('ж', 0, right_hand.fingers['fi5']), # № 39
        Key('э', 0.5, right_hand.fingers['fi5']), # № 40 right_hand
        Key('\n', 1, right_hand.fingers['fi5']), # № 28 right_hand
    ])

    upper_row = Row('UPPER', [Key('й', 2, left_hand.fingers['fi5']), # №16 left_hand
        Key('ц', 2, left_hand.fingers['fi4']), # № 17
        Key('у', 2, left_hand.fingers['fi3']), # № 18
        Key('к', 2, left_hand.fingers['fi2']), # № 19
        Key('е', 2.5, left_hand.fingers['fi2']),# № 20 left_hand

        Key('н', 3, right_hand.fingers['fi2']), # 21right_hand
        Key('г', 2, right_hand.fingers['fi2']), # № 22

        Key('ш', 2, right_hand.fingers['fi3']), # № 23
        Key('щ', 2, right_hand.fingers['fi4']), # № 24

        Key('з', 2, right_hand.fingers['fi5']), # № 25
        Key('х', 2.5, right_hand.fingers['fi5']), # № 26
        Key('ъ', 3, right_hand.fingers['fi5']), # № 27
        Key(['\\', '/'], 3.5, right_hand.fingers['fi5']), # № 43 right_hand
    ])

    lower_row = Row('LOWER', [Key('я', 2.5, left_hand.fingers['fi4']),# №44 left_hand
        Key('ч', 2.5, left_hand.fingers['fi3']), # №45
        Key('с', 2.5, left_hand.fingers['fi2']), # №46
        Key('м', 2.5, left_hand.fingers['fi2']), # №47
        Key('и', 3, left_hand.fingers['fi2']), # №48 left_hand

        Key('т', 2.5, right_hand.fingers['fi2']), # № 49 right_hand
        Key('ь', 2.5, right_hand.fingers['fi2']), # № 50
        Key('б', 2.5, right_hand.fingers['fi3']), # № 51
        Key('ю', 2.5, right_hand.fingers['fi4']), # № 52
        Key(['.', ','], 2.5, right_hand.fingers['fi5']), # № 53 
    ])

    # Нагрузка по руку и на пальцы
    left_hand.print_result()
    right_hand.print_result()

    # Нагрузка на ряды
    digital_row.print_result()
    home_row.print_result()
    upper_row.print_result()
    lower_row.print_result()

    # digital_row.print_info()
    # home_row.print_info()
    # upper_row.print_info()
    # lower_row.print_info()
if __name__ == '__main__':
    main()

# first_row = [Key('й', 2, Finger('little_finger')), Key('ц', 2 ), Key('у', 2 ), Key('к', 2 ), Key('е', 2.5 ), Key('н', 3 ), Key('г', 2 )]
# upper_row = Row()












'''Если добавить палец, который наживает на определенную клавишу, то число нажатий на главишу будет ровняться числу нагрузке пальца.
    рука будет иметь словарь из пальцев "Имя пальца" : "Объект пальца"
    Теперь палец будет иметь получать в конструктор только имя.
'''


'''
В этой модели клавиша имеет: 
    
'''

'''
Нагрузка считается на клавишу. И нагрузка пальца равна нагрузке клавиши.

1. Будет 4 ряда, к которых расположены клавиши.
2. В этой модели клавиша имеет: 
    имя; штраф; палец, котoрый на нее нажимает;
3. При создании ряда задействован палец, но палец должен быть у руки. Для подсчета нагрузки на руку используется словарь из пальце.
4. Для подсчета нагрузки на ряд, нужно в передавать список клавиш для ряда.
'''
