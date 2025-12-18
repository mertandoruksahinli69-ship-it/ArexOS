#include <stdio.h>
#include "kernel.h"
#include "task.h"
#include "fs.h"

void kernel_init() {
    printf("[KERNEL] ArexKernel baslatildi\n");
    task_init();
    fs_init();
}

void kernel_run() {
    printf("[KERNEL] Kernel calisiyor...\n");
    task_run();
}
