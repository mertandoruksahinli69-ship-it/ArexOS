#include <stdio.h>
#include "fs.h"

void fs_init() {
    printf("[FS] Sanal dosya sistemi yuklendi\n");
}

void fs_list() {
    printf("[FS] /system\n");
    printf("[FS] /apps\n");
    printf("[FS] /user\n");
}
