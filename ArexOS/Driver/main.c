#include <string.h>
#include "driver.h"
#include "py_driver.h"
#include "java_driver.h"
#include "exe_driver.h"

void dispatch(const char* path) {

    if (strstr(path, ".py"))
        PY_DRIVER.open(path);

    else if (strstr(path, ".java") || strstr(path, ".jar"))
        JAVA_DRIVER.open(path);

    else if (strstr(path, ".exe"))
        EXE_DRIVER.open(path);
}

int main() {
    dispatch("test.py");
    // dispatch("app.jar");
    // dispatch("program.exe");
    return 0;
}
