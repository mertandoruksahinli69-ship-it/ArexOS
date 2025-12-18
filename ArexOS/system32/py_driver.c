#include <stdio.h>
#include "driver.h"

void py_open(const char* path) {
    printf("[PY_DRIVER] '%s' dosyası açıldı.\n", path);
}

Driver PY_DRIVER = {
    "Python Driver",
    py_open
};
