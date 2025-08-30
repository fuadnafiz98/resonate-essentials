from resonate import Resonate
import random


# Initialize Resonate with a local store (in memory)
resonate = Resonate()


@resonate.register
def download_and_summarize(ctx, url):
    print("running download_and_summarize")
    content = yield ctx.run(download, url)
    summary = yield ctx.run(summarize, content)
    return summary

def download(_, url):
    print("running download")
    if random.randint(0, 100) > 50:
        raise Exception("download encountered an error")
    return f"content of {url}"


def summarize(_, content):
    print("running summarize")
    if random.randint(0, 100) > 50:
        raise Exception("summarize encountered an error")
    return f"summary of {content}"


def main():
    try:
        url = "https://example.com"
        handle = download_and_summarize.begin_run(url, url=url)
        print(handle.result())
    except Exception as e:
        print(e)

# Run the main function when the script is invoked
if __name__ == "__main__":
    main()
