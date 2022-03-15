#include <unistd.h>
#include <main.h>

/**
 * _putchar - writes the character c to stdout
 * @c: The character to prin
 *
 * Return: On success 1.
 * On error, -1 is returned, and errno is set appropriately.
 */
nt main(void)
{
	char text[9] = "_putchar";
	int i;
	for (i = 0; i < 9; i++)
	{
		_putchar(text[i]);
	}
	_putchar('\n');
	return (0);
}
