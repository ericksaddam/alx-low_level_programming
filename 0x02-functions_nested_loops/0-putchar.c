#include <unistd.h>
#include "main.h"

/**
 * main - Function main entry
 *
 * Program that prints _putchar, followed by a new line
 *
 * Return: always 0 (success)
 */

int main(void)
{
	char s[9] = "_putchar";
	int i;

	for (i = 0; i < 9; i++)
	{
		_putchar(text[i]);
	}

	_putchar('\n');

	return (0);
}
