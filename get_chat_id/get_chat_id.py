import json


def get_id(message, chat_ids):
    new_id = {'chat_id': message.chat.id}
    have = False
    for i in chat_ids:
        if i == new_id:
            have = True
    if not have:
        chat_ids.append(new_id)
    print(chat_ids)
    with open('users.json', 'w') as jsonFile:
        json.dump(chat_ids,
                  jsonFile,
                  sort_keys=True,
                  ensure_ascii=False,
                  indent=2,
                  )
