#include <stddef.h>
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
*creat_list
*@n: number
*@old: old list
*@len: length of the list
*Return: new list
*/
int *creat_list(int n, int **list, int len)
{
	int *new = NULL, idx = 0;

	new = malloc(sizeof(int) * len);
	if (new == NULL)
	{
		free(*list);
		return (NULL);
	}
	while (len - 1)
	{
		new[idx] = (*list)[idx];
		len--;
		idx++;
	}
	new[idx] = n;
	free(*list);
	return (new);
}
/**
*is_palindrome
*@head: head of the linked list
*Return: return 0 if the list is not a palindrom and 1 if it is
*/
int is_palindrome(listint_t **head)
{
	int idx = 0, idx2 = 0, *list = NULL, len = 0, is_pal = 0;
	listint_t *ptr, *ptr2;
	if (!head || !(*head) || (*head)->next == NULL)
		return (1);
	ptr = *head;
	while (ptr && ptr->next)
	{
		len++;
		list = creat_list(ptr->n, &list, len);
		if (ptr->n == ptr->next->n)
		{
			ptr2 = ptr;
			for (idx2 = idx; idx2 != -1; idx2--)
			{
				ptr2 = ptr2->next;
				if (ptr2->n != list[idx2])
				{
					is_pal = 0;
					break;
				}
				else
					is_pal = 1;
			}
		}
		if (is_pal == 1)
			break;
		idx++;
		ptr = ptr->next;
	}
	free(list);
	return (is_pal);
}