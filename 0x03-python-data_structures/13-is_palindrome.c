#include <stddef.h>
#include "lists.h"

/**
 * reverse_second_half - reverses the second half of the list
 *
 * @second_half: head of the second half
 * Return: no return
 */
void reverse_second_half(listint_t **second_half)
{
listint_t *prev = NULL;
listint_t *current = *second_half;
listint_t *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*second_half = prev;
}

/**
 * compare_lists - compares each int of the list
 *
 * @list1: head of the first half
 * @list2: head of the second half
 * Return: 1 if they are equal, 0 if not
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
listint_t *ptr1 = list1;
listint_t *ptr2 = list2;

while (ptr1 != NULL && ptr2 != NULL)
{
if (ptr1->n == ptr2->n)
{
ptr1 = ptr1->next;
ptr2 = ptr2->next;
}
else
{
return (0);
}
}

if (ptr1 == NULL && ptr2 == NULL)
{
return (1);
}

return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev_slow = *head;
listint_t *second_half = NULL;
listint_t *mid_node = NULL;
int is_palindrome = 1;

if (*head != NULL && (*head)->next != NULL)
{
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}

if (fast != NULL)
{
mid_node = slow;
slow = slow->next;
}

second_half = slow;
prev_slow->next = NULL;
reverse_second_half(&second_half);
is_palindrome = compare_lists(*head, second_half);

if (mid_node != NULL)
{
prev_slow->next = mid_node;
mid_node->next = second_half;
}
else
{
prev_slow->next = second_half;
}
}

return (is_palindrome);
}

