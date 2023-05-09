#ifndef _LISTS_H_
#define _LISTS_H_


#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

#endif