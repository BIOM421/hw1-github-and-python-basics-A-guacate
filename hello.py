def hello_world():
	return "Hello World!"

def hello_world_n(N):
    result = ""
    for _ in range(N):
        if _ < N - 1:
            result += "Hello World! "
        else:
            result += "Hello World!"
    return result



## Mini test
# result1 = hello_world()
# print(result1)
# result2 = hello_world_n(5)
# print(result2)