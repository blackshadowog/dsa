def fun(n):
    if n == 0:
        return

    print("Going:", n)
    fun(n - 1)
    print("Coming back:", n)

fun(3)