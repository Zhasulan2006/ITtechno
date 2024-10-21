[app]
# Имя вашего приложения
title = IT-Tech

# Название пакета
package.name = it_tech

# Домен пакета
package.domain = space.tolegenov

# Главный скрипт
source.include_exts = py,png,jpg,kv,atlas

# Путь к главному Python файлу
source.main = main.py

# Иконка приложения
icon.filename = %(source.dir)s/logo.png

# Версия приложения
version = 0.1

# Список зависимостей (требуемых библиотек)
requirements = python3,kivy==2.2.1,kivymd==1.2.0

# Страница ориентации приложения (portrait, landscape, sensor)
orientation = portrait

# Минимальная версия Android
android.minapi = 21

# Разрешенные права доступа
android.permissions = INTERNET

# (опционально) Указать поддерживаемые архитектуры
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# Установить log_level на 2 для более подробного вывода
log_level = 2
