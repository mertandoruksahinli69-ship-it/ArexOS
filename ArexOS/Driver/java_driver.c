#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "java_driver.h"

void java_open(const char* path) {
    char cmd[512];

    if (strstr(path, ".jar"))
        snprintf(cmd, sizeof(cmd), "java -jar \"%s\"", path);
    else
        snprintf(cmd, sizeof(cmd), "javac \"%s\"", path);

    system(cmd);
}

Driver JAVA_DRIVER = {
    "Java Driver",
    java_open
};
