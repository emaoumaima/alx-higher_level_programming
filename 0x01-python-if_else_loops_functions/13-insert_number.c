#include "lists.h"

/**
 * insert_node - add node to list
 * @head: head
 * @number: where to add
 * Return: adss or null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *previous;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (head == NULL || *head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	current = *head;
	previous = NULL;

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}
	if (previous == NULL)
	{
		new_node->next = current;
		*head = new_node;
	}
	else
	{
		new_node->next = current;
		previous->next = new_node;
	}
	return (new_node);
}
