import datetime


def get_format_week(week_id):
    if isinstance(week_id, int):
        current_week = datetime.datetime.today().weekday()
        right_week_id = week_id - current_week
        if right_week_id < 0:
            weeks = 1
        else:
            weeks = 0
        return (datetime.datetime.today() + datetime.timedelta(days=right_week_id, weeks=weeks)).strftime("%d.%m.%Y")

    elif isinstance(week_id, str):
        if week_id.lower() == "yesterday":
            return (datetime.datetime.today() + datetime.timedelta(days=-1)).strftime("%d.%m.%Y")
        if week_id.lower() == "today":
            return datetime.datetime.today().strftime("%d.%m.%Y")
        if week_id.lower() == "tomorrow":
            return (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")
