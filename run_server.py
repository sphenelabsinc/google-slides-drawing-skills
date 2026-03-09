from authentication import ensure_credentials

from server.server import run


def main():
    ensure_credentials()
    run()


if __name__ == "__main__":
    main()
