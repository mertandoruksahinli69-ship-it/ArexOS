; minimal ASM rutinleri, sadece simülasyon
section .text
global _start

_start:
    ; Merhaba mesajı
    mov rax, 1          ; write
    mov rdi, 1          ; stdout
    mov rsi, msg
    mov rdx, msg_len
    syscall
    ret

section .data
msg db "ArexOS ASM Kernel Simülasyonu", 0xA
msg_len equ $ - msg
