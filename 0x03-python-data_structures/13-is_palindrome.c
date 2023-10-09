#include <stddef.h>
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
*is_palindrome
*@head: head of the linked list
*Return: return 0 if the list is not a palindrom and 1 if it is
*/
int is_palindrome(listint_t **head)
{
	int idx = 0, *list = NULL, len = 0;
	listint_t *ptr = NULL;

	if (!head || !(*head) || (*head)->next == NULL)
		return (1);
	ptr = *head;
	while (ptr)
	{
		len++;
		ptr = ptr->next;
	}
	list = malloc(sizeof(int) * len);
	ptr = *head;
	while (ptr)
	{
		list[idx] = ptr->n;
		idx++;
		ptr = ptr->next;
	}
	ptr = *head;
	idx--;
	while (ptr)
	{
		if (ptr->n != list[idx])
		{
			free(list);
			return (0);
		}
		ptr = ptr->next;
		idx--;
	}
	free(list);
	return (1);
}
