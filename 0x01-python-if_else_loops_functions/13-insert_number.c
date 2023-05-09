#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to a pointer to the head of the list.
 * @number: The number to insert.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current;

if (head == NULL)
return (NULL);

/* Create a new node */
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);
new_node->n = number;
new_node->next = NULL;

/* Insert the new node into the list */
if (*head == NULL)
{
/* If the list is empty, insert at the head */
*head = new_node;
}
else if (number < (*head)->n)
{
/* If the new node is smaller than the head, insert at the head */
new_node->next = *head;
*head = new_node;
}
else
{
/* Otherwise, find the correct position to insert the new node */
current = *head;
while (current->next != NULL && number > current->next->n)
current = current->next;
new_node->next = current->next;
current->next = new_node;
}

return (new_node);
}
