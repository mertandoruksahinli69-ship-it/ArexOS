#include <stdio.h>
#include "driver.h"

void java_open(const char* path) {
    printf("[JAVA_DRIVER] '%s' dosyası açıldı.\n", path);
}

Driver JAVA_DRIVER = {
    "Java Driver",
    java_open
};
