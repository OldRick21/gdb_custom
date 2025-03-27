set disassembly-flavor intel
tui new-layout asm-debug {-horizontal src 1 regs 1} 2 status 0 cmd 1
set auto-load safe-path /
source /home/s1berian_rat/.config/gdb/gdb-custom-commands.py
