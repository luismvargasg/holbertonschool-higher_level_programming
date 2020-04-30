#include "lists.h"

/**
 * insert_node - func. that inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the list.
 * @number: value to store in the new node.
 *
 * Return: Pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *cursor = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL || cursor->n >= number)
	{
		*head = new_node;
		new_node->next = cursor;
	}
	else
	{
		while (cursor->next != NULL)
		{
			if (cursor->next->n <= number)
				cursor = cursor->next;
			else
				break;
		}
	}
	return (new_node);
}
