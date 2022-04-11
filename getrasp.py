import json
import requests
import time
from termcolor import cprint


def get_timetable_json():
    while True:
        rasp = json.loads(requests.get('https://timetable.tusur.ru/api/v2/raspisanie_vuzov').text)
        with open('rasp.json', 'w') as jsonFile:
            json.dump(rasp['faculties'][3]['groups'][28]['lessons'],
                      jsonFile,
                      sort_keys=True,
                      ensure_ascii=False,
                      indent=2,
                      )
        cprint('OK', 'green')
        time.sleep(1800)
