#include <stdio.h>
#include <stdlib.h>
#include "python_reader.h"

void run_python(const char* path) {
    char command[512];
    snprintf(command, sizeof(command), "python \"%s\"", path);
    system(command);
}
