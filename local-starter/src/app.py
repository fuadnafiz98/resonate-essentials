from resonate import Resonate, Context
import time


# Initialize Resonate with a local store (in memory)
resonate = Resonate()


# Register the top-level function with Resonate
@resonate.register
def foo(ctx: Context, greeting: str):
    print("running foo")
    # to make this call asynchronous
    promise = yield ctx.begin_run(bar, greeting)
    print("P", promise)
    greeting = yield promise
    print("R", greeting)
    greeting = yield ctx.run(baz, greeting)
    return greeting


def bar(_, v):
    print("running bar")

    return f"{v} world"


def baz(_, v):
    print("running baz")
    return f"{v}!"


# Define a main function
def main():

    resonate.start()

    handles = resonate.begin_run(f"test-foo-lfi", "foo", f"hello-world")

    results = handles.result()

    print(results)


# Run the main function when the script is invoked
if __name__ == "__main__":
    main()
