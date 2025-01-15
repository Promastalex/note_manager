username = input("Введите свое имя: " )
print(f"Имя пользователя: {username}")
title = input("Введите заголовок заметки: ")
print(f"Заголовок заметки: {title}")
content = input("Введите описание заметки: ")
print(f"Описание заметки: {content}")
status = input("Введите статус заметки: ")
print(f"Статус заметки: {status}")
created_date = input(f"Введите дату создания заметки: ")
issue_date = created_date [0:6]
print(f"Дата создания заметки: {issue_date}")
issue_data = input("Введите дату истечения заметки ")
created_date = issue_data [0:6]
print(f"Дата истечения заметки: {created_date}")