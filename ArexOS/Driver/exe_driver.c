#include <windows.h>
#include <stdio.h>
#include "exe_driver.h"

void exe_open(const char* path) {
    ShellExecuteA(NULL, "open", path, NULL, NULL, SW_SHOW);
}

Driver EXE_DRIVER = {
    "EXE Driver",
    exe_open
};
