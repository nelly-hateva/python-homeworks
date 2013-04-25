ZODIAC = {
    range(321, 421): 'Овен',
    range(421, 521): 'Телец',
    range(521, 621): 'Близнаци',
    range(621, 722): 'Рак',
    range(722, 823): 'Лъв',
    range(823, 923): 'Дева',
    range(923, 1023): 'Везни',
    range(1023, 1122): 'Скорпион',
    range(1122, 1222): 'Стрелец',
    range(1222, 1232): 'Козирог',
    range(101, 120): 'Козирог',
    range(120, 219): 'Водолей',
    range(219, 321): 'Риби',
}


def what_is_my_sign(day, month):
    for range_, sign in ZODIAC.items():
        if month * 100 + day in range_:
            return sign
