#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a list
 * @list: pointer to list to check
 *
 * Return: 0 if no cycle 1 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *bunch1 = list, *bunch2 = list;

	while (bunch1 && bunch1->next)
	{
		bunch2 = bunch2->next;
		bunch1 = bunch1->next->next;
		if (bunch1 == bunch2)
			return (1);
	}
	return (0);
}
