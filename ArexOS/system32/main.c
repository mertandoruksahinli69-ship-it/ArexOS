#include <stdio.h>
#include <string.h>
#include "driver.h"

// Driver’ları include et
#include "py_driver.c"
#include "java_driver.c"
#include "exe_driver.c"

// Config simülasyonu
void load_config(const char* cfg_path) {
    printf("Config dosyası yükleniyor: %s\n", cfg_path);
    // Burada cfg dosyasını okuyup işlem yapabilirsin
}

// Driver dispatcher
void dispatch(const char* path) {
    if (strstr(path, ".py"))
        PY_DRIVER.open(path);
    else if (strstr(path, ".java") || strstr(path, ".jar"))
        JAVA_DRIVER.open(path);
    else if (strstr(path, ".exe"))
        EXE_DRIVER.open(path);
    else
        printf("[SYSTEM] '%s' bilinmeyen dosya türü.\n", path);
}

int main() {
    load_config("config/system.cfg");
    load_config("config/drivers.cfg");

    // Test dosyaları
    dispatch("script.py");
    dispatch("app.jar");
    dispatch("program.exe");
    dispatch("image.gfx"); // bilinmeyen tür

    return 0;
}
