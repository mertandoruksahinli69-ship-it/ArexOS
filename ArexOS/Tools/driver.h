#ifndef DRIVER_H
#define DRIVER_H

typedef struct {
    const char* name;
    void (*open)(const char* path);
} Driver;

#endif
