# GDB Debugging Setup for Assembly Matrix Project

## Файловая структура

project/
├── .gdbinit # Конфигурация GDB
├── gdb-custom-commands.py # Пользовательские команды GDB
├── debug-script.gdb # Скрипт отладки
└── program.asm # Ваш ассемблерный код


## Настройка окружения

    1. Установите зависимости:
       
        ```bash
        sudo apt-get install gdb nasm gcc-multilib
        ```
    
    2. Разместите файлы:
       
        ```bash
        mkdir -p ~/.config/gdb
        mv gdb-custom-commands.py ~/.config/gdb/
        mv .gdbinit ~/
        mv debug-script.gdb ./
        ```
    
    3. Скомпилируйте программу:
       
        ```bash
        nasm -f elf64 -g -F dwarf program.asm -o program.o
        ld program.o -o program
        ```

Использование

    Базовая отладка
    
        ```bash
        gdb -q ./program -x debug-script.gdb
        ```

Ключевые команды в GDB:

    pm - Показать матрицу в реальном времени

    layout asm-debug - Переключить вид с исходным кодом и регистрами

    ni - Шаг с обходом вызовов (next instruction)

    si - Шаг с заходом в вызовы (step instruction)

Описание файлов

    1. .gdbinit
   
       ```text
       set disassembly-flavor intel       # Использовать Intel-синтаксис
       tui new-layout asm-debug {         # Кастомный интерфейс:
           asm 1                          # Верхняя панель: ассемблерный код
           regs 1                         # Нижняя панель: регистры + команды
           cmd 1
       }
       source ~/.config/gdb/gdb-custom-commands.py # Подключение кастомных команд
       ```
   
    2. gdb-custom-commands.py
    
       ```python
        class PMCommand(gdb.Command):    # Реализация команды 'pm'
        """Чтение rows/cols из памяти
        Расчет смещений для матрицы 3x5
        Форматированный вывод со знаком"""
        # ... (реализация команды)
       ```

    3. debug-script.gdb
   
       ```text
        layout asm-debug   # Активация кастомного интерфейса
        b _start           # Точка останова на начале программы
        run                # Запуск программы
       ```

Пример сессии отладки

    Запустите отладчик:

        ```bash
        gdb -q ./program -x debug-script.gdb
        
            После остановки на _start:
        ```
        
        ```text
        (gdb) pm
        Matrix (3x5):
        [   12,    -5,     7,     3,     0]
        [    4,     9,    -2,     6,     1]
        [   -1,     8,    15,     2,    -3]
        ```
        
    Для пошагового выполнения:

        ```text
        (gdb) ni  # Next Instruction
        (gdb) si  # Step Instruction
        ```
Решение проблем

    Если не загружаются кастомные команды:
    
        ```bash
        echo "source ~/.config/gdb/gdb-custom-commands.py" >> ~/.gdbinit
    ```
    
    Для проверки путей:
    
        ```bash
        gdb -nx -ex 'show auto-load' -ex 'quit'
        ```
    Если возникает ошибка формата:
    
        ```bash
        rm ~/.gdbinit && cp .gdbinit ~/
        ```
        
Данная конфигурация оптимизирована для:

    x86_64 архитектуры

    NASM синтаксиса

    GDB версии 9.2+

    Linux-окружения

   





