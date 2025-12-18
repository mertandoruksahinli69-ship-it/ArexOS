#include <stdlib.h>
#include <stdio.h>
#include "py_driver.h"

void py_open(const char* path) {
    char cmd[512];
    snprintf(cmd, sizeof(cmd), "python \"%s\"", path);
    system(cmd);
}

Driver PY_DRIVER = {
    "Python Driver",
    py_open
};
