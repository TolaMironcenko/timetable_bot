from number_of_pare import number_of_pare


def getpare(day, pare, data):
    pare += number_of_pare(data['time']['start'])[1] + ' ' + \
           data['subject'] + '\n'
    if data['type'] == 'Лекция':
        pare += '🧑‍🏫 ' + data['type'] + '\n'
    elif data['type'] == 'Практика':
        pare += '🤲 ' + data['type'] + '\n'
    elif data['type'] == 'Лабораторная работа':
        pare += '🥼 ' + data['type'] + '\n'
    pare += '⏳ ' + data['time']['start'] + '-' + \
            data['time']['end'] + '\n'
    pare += '🧍 '
    for j in data['teachers']:
        pare += j['name'] + ' '
    pare += '\n'
    if data['audiences']:
        pare += '🏛 '
        for a in data['audiences']:
            pare += a['name'] + ' '
        pare += '\n'
    for i in data['note_by_date']:
        if day == i['date']:
            if i['note'] == 'реализуется в эиос':
                pare += '💻 ' + i['note'] + '\n'
            else:
                if i['note'] != '':
                    pare += '👯‍ ' + i['note'] + '\n'
    pare += '\n'

    return pare


def rasptoeveryday(day, data):

    pares = ['', '', '', '', '', '', '', '']

    for i in data:
        if i['date'].find(day) != -1:
            for j in range(1, 8):
                if number_of_pare(i['time']['start'])[0] == str(j):
                    pares[j] = getpare(day, pares[j], i)
            pares[0] = pares[1] + pares[2] + pares[3] + \
                pares[4] + pares[5] + pares[6] + pares[7]
    if pares[0] == '':
        return 'ещё нет расписания на этот день'
    else:
        return pares[0]
