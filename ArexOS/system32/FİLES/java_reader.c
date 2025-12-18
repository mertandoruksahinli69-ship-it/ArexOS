#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "java_reader.h"

void run_java(const char* path) {
    char command[512];

    if (strstr(path, ".java")) {
        snprintf(command, sizeof(command), "javac \"%s\"", path);
        system(command);
    } 
    else if (strstr(path, ".jar")) {
        snprintf(command, sizeof(command), "java -jar \"%s\"", path);
        system(command);
    }
}
