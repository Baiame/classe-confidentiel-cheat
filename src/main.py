import argparse

from request import Request

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make some post requests on the url")
    parser.add_argument("--url", help="url of the web page")
    parser.add_argument("--dictionary", help="path to .txt dictionary file")
    args = parser.parse_args()

    req = Request(args.url, args.dictionary)
    req.run()
