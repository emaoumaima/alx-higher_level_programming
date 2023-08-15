#include "lists.h"

/**
 * is_palindrome - check if is palindrom
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 or 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head,
	*prev = NULL, *curr, *next, *first, *second;

	if (*head == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	curr = slow;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	first = *head;
	second = prev;
	while (first != NULL && second != NULL)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}
	return (1);
}
