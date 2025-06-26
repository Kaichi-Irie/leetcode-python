# %%
import functools


def cache(function):
    results_cache = {}

    @functools.wraps(function)
    def wrapper(*args, **kwargs):

        # The key must be the same, regardless of the order in which the keyword arguments are given.
        key = (args, tuple(sorted(kwargs.items())))
        print(f"{key=}")
        if key in results_cache:
            print("cache is used")
            return results_cache[key]
        result = function(*args, **kwargs)
        results_cache[key] = result
        return result

    return wrapper


# %%
import time


@cache
def my_func(
    i: int,
    kw_x: str = "keyword X",
    kw_y: str = "keyword Y",
) -> str:
    return f"{time.time()}, {kw_x=}, {kw_y=}"


# %%


print(my_func(1, kw_x="x", kw_y="y"))
# %%
print(my_func(1, kw_y="y", kw_x="x"))  # cache should be used


print(my_func(1))

# %%
print(my_func(1))

# %%
print(my_func(1))

# %%
tp = (1, 2, 3)
tp_ = (4, 5)
tp += tp_
print(tp)  # (1, 2, 3, 4, 5)

# %%
import functools


@functools.cache
def myfunc(a=-1, b=-1, c=-1):
    print("my func is called")
    return 0


# %%
myfunc(a=1, b=2)  # my func is called
myfunc(b=2, a=1)  # my func is called

# %%
myfunc(a=1, b=2)  # nothing
# %%
myfunc(b=1)  # myfunc(b=1, a=-1)と同じ扱い
myfunc(a=-1, b=1)


# %%
import timeit

# キーワード引数が5個の場合
kwargs_small = {f"k{i}": i for i in range(5)}
# キーワード引数が20個の場合
kwargs_large = {f"k{i}": i for i in range(20)}


# ソートしない場合 (現在の functools.cache の方式)
def no_sort(kwargs):
    return tuple(kwargs.items())


# ソートする場合 (ご自身の提案、および古いPythonの方式)
def do_sort(kwargs):
    return tuple(sorted(kwargs.items()))


# 計測
time_no_sort_small = timeit.timeit(lambda: no_sort(kwargs_small), number=1_000_000)
time_do_sort_small = timeit.timeit(lambda: do_sort(kwargs_small), number=1_000_000)

time_no_sort_large = timeit.timeit(lambda: no_sort(kwargs_large), number=1_000_000)
time_do_sort_large = timeit.timeit(lambda: do_sort(kwargs_large), number=1_000_000)

print(f"--- キーワード引数: 5個 (100万回実行) ---")
print(f"ソートなし: {time_no_sort_small:.4f} 秒")
print(f"ソートあり: {time_do_sort_small:.4f} 秒")
print(f"パフォーマンス差: {time_do_sort_small / time_no_sort_small:.2f} 倍遅い")
print("\n")
print(f"--- キーワード引数: 20個 (100万回実行) ---")
print(f"ソートなし: {time_no_sort_large:.4f} 秒")
print(f"ソートあり: {time_do_sort_large:.4f} 秒")
print(f"パフォーマンス差: {time_do_sort_large / time_no_sort_large:.2f} 倍遅い")

# %%
