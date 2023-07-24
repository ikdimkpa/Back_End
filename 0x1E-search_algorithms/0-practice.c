#include "search_algos.h"
#include <stdio.h>

/**
 * linear_search - Searches for a value in an array of integers using the Linear search algorithm
 * @array: Pointer to the first element of the array
 * @size: Number of elements in array
 * @value: value to search for
 *
 * Return: Index where value is located or -1 if value is not present in array or if array is NULL
 */
int linear_search(int *array, size_t size, int value)
{
	unsigned int index;

	if (!array || size == 0)
		return (-1);

	for (index = 0; index < size; index++)
	{
		do
		{
			printf("Value checked at array[%d] = [%d]\n", index, array[index]);
			index++;
		} while (array[index] != value && index < size);
		printf("\n");

		if (array[index] == value)
			return (index);
	}

	return (-1);
}
