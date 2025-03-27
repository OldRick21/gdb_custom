import gdb

class PMCommand(gdb.Command):
    def __init__(self):
        super(PMCommand, self).__init__("pm", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        try:
            # Получаем размеры матрицы
            rows = int(gdb.parse_and_eval("*(unsigned char*)&rows"))
            cols = int(gdb.parse_and_eval("*(unsigned char*)&cols"))
            
            # Явно получаем адрес матрицы как целое число
            matrix_addr = int(gdb.parse_and_eval("&matrix"))  # Исправлено здесь!
            inferior = gdb.selected_inferior()
            
            print(f"Matrix ({rows}x{cols}):")
            
            # Ручной расчет адресов
            for i in range(rows):
                row = []
                for j in range(cols):
                    offset = (i * cols + j) * 2  # 2 байта на элемент (short)
                    current_addr = matrix_addr + offset
                    
                    # Чтение 2 байт как знакового short
                    bytes_data = inferior.read_memory(current_addr, 2).tobytes()
                    val = int.from_bytes(bytes_data, byteorder='little', signed=True)
                    row.append(f"{val:5}")
                    
                print("[" + ", ".join(row) + "]")
                
        except Exception as e:
            print(f"Error: {e}")

PMCommand()
