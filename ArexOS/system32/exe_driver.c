#include <stdio.h>
#include "driver.h"

void exe_open(const char* path) {
    printf("[EXE_DRIVER] '%s' dosyası açıldı.\n", path);
}

Driver EXE_DRIVER = {
    "EXE Driver",
    exe_open
};
