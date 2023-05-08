#ifndef LISTS_H_
#define LISTS_H_

#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list */
typedef struct node
{
int data;
struct node* next;
} listint_t;

int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
#endif