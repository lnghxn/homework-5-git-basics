def date_format(date_str: str):
    month, day, year = date_str.split('/')
    return f"{year}-{month}-{day}"