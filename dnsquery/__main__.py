import os, sys
from . import dnsquery

def main():
    """The entry point of the module when run as a script."""
    if sys.argv.__len__() < 2:
        raise Exception("Please provide at least 1 domain name to query")
    answers = dnsquery(
        qnames=sys.argv[1:],
    )
    print("\n".join(answers))

if __name__ == "__main__":
    if __package__ == "":
        # if the package is run directly with the folder, add
        # the parent folder as part of PYTHONPATH for the
        # current execution environment so the uninstalled
        # "dnsquery" package is discoverable.
        sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

    try:
        main()
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)