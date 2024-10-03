import click

import binascii
from colorama import Style, Fore
from typing import cast

def decode_json_file(path: str) -> str:
    try:
        with open(path, "r") as f:
            print(f"Decoding '{Fore.CYAN}{path}{Style.RESET_ALL}'... ", end="")
            s = binascii.unhexlify(f.readline()).decode("utf-8")
            print(f"{Fore.GREEN}OK{Style.RESET_ALL}")
            return s
    except Exception as e:
        print(f"{Fore.RED}ERROR{Style.RESET_ALL}")
        print(f"Error: {e}")

    return ""

@click.command(
    short_help="Tool that receives a series of files pertaining to a set of earbuds containing the json string in hex and merges them into one."
)
@click.argument("src", required=True, nargs=-1)
@click.argument("dst", required=True)
def cli(src: tuple[str], dst: str) -> None:
    parts: list[str] = []
    for f in src:
        parts.append(decode_json_file(f))

    with open(dst, "w") as out:
        out.write(f"[{','.join(parts)}]")

    print("Merged ", end="")
    for i, f in enumerate(src):
        print(f"{Fore.CYAN}{f}{Style.RESET_ALL}", end="")
        if i != len(src) - 1:
            print(", ", end="")
    print(f" into '{Fore.CYAN}{dst}{Style.RESET_ALL}'... {Fore.GREEN}OK{Style.RESET_ALL}")

if __name__ == "__main__":
    cli()
