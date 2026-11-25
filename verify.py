from argparse import ArgumentParser
from pathlib import Path


def main():
    parser = ArgumentParser()
    parser.add_argument("mode", choices=("quick", "full"))
    args = parser.parse_args()
    data = Path(__file__).resolve().parent / "data"
    parts = {name: (data / f"{name}.txt").read_text(encoding="utf-8").strip() for name in ("left", "right")}
    if any(value not in {"1", "2"} for value in parts.values()):
        raise SystemExit("Each part must be 1 or 2")
    total = sum(map(int, parts.values()))
    if args.mode == "full" and total > 3:
        raise SystemExit(f"Combined limit failed: left={parts['left']} right={parts['right']} total={total} limit=3")
    print(f"{args.mode} passed: left={parts['left']} right={parts['right']} total={total}")


if __name__ == "__main__":
    main()
