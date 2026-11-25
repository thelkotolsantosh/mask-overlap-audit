"""Score aligned CSV label masks, one row per image scanline."""
import argparse
import csv
import json
from collections import Counter
from itertools import zip_longest


def score(reference, prediction, ignore=None):
    truth, guessed, hits = Counter(), Counter(), Counter()
    width = None
    for line, (a, b) in enumerate(zip_longest(reference, prediction), 1):
        if a is None or b is None:
            raise ValueError(f"height mismatch at row {line}")
        if width is None:
            width = len(a)
        if not width or len(a) != width or len(b) != width:
            raise ValueError(f"width mismatch or empty row at row {line}")
        for actual, predicted in zip(a, b):
            actual, predicted = actual.strip(), predicted.strip()
            if not actual or not predicted:
                raise ValueError(f"empty label at row {line}")
            if actual == ignore:
                continue
            truth[actual] += 1
            guessed[predicted] += 1
            if actual == predicted:
                hits[actual] += 1
    if not truth:
        raise ValueError("no scored pixels")
    classes = {}
    for label in sorted(truth.keys() | guessed.keys()):
        union = truth[label] + guessed[label] - hits[label]
        classes[label] = {"intersection": hits[label], "union": union,
                          "iou": hits[label] / union}
    return {"pixels": sum(truth.values()), "classes": classes,
            "mean_iou": sum(c["iou"] for c in classes.values()) / len(classes)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference")
    parser.add_argument("prediction")
    parser.add_argument("--ignore", help="exclude pixels with this reference label")
    args = parser.parse_args()
    try:
        with open(args.reference, newline="", encoding="utf-8-sig") as a, open(
                args.prediction, newline="", encoding="utf-8-sig") as b:
            result = score(csv.reader(a, strict=True), csv.reader(b, strict=True), args.ignore)
    except (ValueError, OSError, csv.Error) as exc:
        parser.exit(2, f"mask audit: {exc}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
