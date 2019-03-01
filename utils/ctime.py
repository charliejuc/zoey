from time import time

def speed_test(func, times=1000, print_results=True):
	start = time()

	for i in range(0, times):
		func()

	end = time()

	t = end - start

	if print_results:
		print(
			'{time} secs in {times} loops.'\
				.format(time=t, times=times)
		)

	return t