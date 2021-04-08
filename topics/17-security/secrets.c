#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    char *secrets[] = {
        "Mississippi",
        "Kansas"
    };
    char *names[] = {
        "George",
        "Travis"
    };

    if (argc > 1) {
        long index = strtol(argv[1], NULL, 10);
        char *name = names[index];
        printf("Name: %s\n", name);
    } else {
        printf("Usage: ./secrets <INDEX>\n");
    }
}
