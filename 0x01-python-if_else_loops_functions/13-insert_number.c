#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
/**
*insert_node - add a new list node at head
*@head :the head of the node
*@number :intger on the node
*Return: a pointer to the head of the list
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *surf;
	int rep = 0;

	if (head == NULL)
		return (NULL);
	surf = *head;
	while (surf && surf->next)
	{
		if (number < surf->n)
		{
			rep = 2;
			break;
		}
		else if (number < surf->next->n ||
			(surf->next == NULL && number > surf->n))
		{
			rep = 1;
			break;
		}
		surf = surf->next;
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		free(new);
		return (NULL);
	}
	new->n = number;
	if (rep == 1)
	{
		new->next = surf->next;
		surf->next = new;
	}
	else
	{
		new->next = *head;
		*head = new;
	}
	return (new);
}
