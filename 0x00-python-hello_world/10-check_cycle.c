#include "lists.h"
#include <stddef.h>
/**
*check_cycle - find a loop in list
*@list : head of the list
*Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *pos1, *pos2;

	if (list == NULL)
		return (0);
	pos1 = list;
	pos2 = list;
	while (pos1 && pos2 && pos2->next)
	{
		pos2 = pos2->next->next;
		pos1 = pos1->next;
		if (pos2 == pos1)
			return (1);
	}
	return (0);
}
