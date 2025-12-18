#include <stdio.h>
#include <string.h>
#include "file_manager.h"
#include "python_reader.h"
#include "java_reader.h"

void open_file(const char* path) {

    if (strstr(path, ".py")) {
        printf("[ArexOS] Python dosyası algılandı\n");
        run_python(path);
    }
    else if (strstr(path, ".java") || strstr(path, ".jar")) {
        printf("[ArexOS] Java dosyası algılandı\n");
        run_java(path);
    }
    else {
        printf("[ArexOS] Desteklenmeyen dosya tipi\n");
    }
}
