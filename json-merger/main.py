import click
import json

from colorama import Style, Fore
from typing import cast

def decode_json_file(path: str) -> dict[str, object]:
    try:
        with open(path, "r") as f:
            print(f"Decoding '{Fore.CYAN}{path}{Style.RESET_ALL}'... ", end="")
            j = json.load(f)
            print(f"{Fore.GREEN}OK{Style.RESET_ALL}")
            return cast(dict[str, object], j)
    except Exception as e:
        print(f"{Fore.RED}ERROR{Style.RESET_ALL}")
        print(f"Error: {e}")

    return {}

@click.command(
    short_help="Tool that receives a series of JSON files pertaining to a set of earbuds and merges them into one."
)
@click.argument("src", required=True, nargs=-1)
@click.argument("dst", required=True)
def cli(src: tuple[str], dst: str) -> None:
    parts: list[dict[str, object]] = []
    for f in src:
        parts.append(decode_json_file(f))

    with open(dst, "w") as out:
        json.dump(parts, out)

    print("Merged ", end="")
    for i, f in enumerate(src):
        print(f"{Fore.CYAN}{f}{Style.RESET_ALL}", end="")
        if i != len(src) - 1:
            print(", ", end="")
    print(f" into '{Fore.CYAN}{dst}{Style.RESET_ALL}'... {Fore.GREEN}OK{Style.RESET_ALL}")

if __name__ == "__main__":
    cli()
