#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: A pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

while (slow != NULL && fast != NULL && fast->next != NULL)
{
slow = slow->next;      /* Moves slow pointer one node at a time */
fast = fast->next->next; /* Moves fast pointer two nodes at a time */

if (slow == fast)
{     /* If there's a cycle, slow and fast pointers will meet */
return (1);           /* Cycle detected */
}
}

return (0);                   /* No cycle detected */
}
