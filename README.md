# Mask Overlap Audit

Evaluate a semantic segmentation model by comparing two aligned CSV masks. A large background region can hide errors on a small object. Per-class intersection over union (IoU) gives each observed class a separate score.

## Setup and example

Use Python 3.10 or newer. Clone or download this repository and open its directory. The standard library supplies every dependency. Run:

```sh
python mask_audit.py examples/reference.csv examples/prediction.csv --ignore void
python -m unittest discover -s tests -v
```

The example compares a road scene with one car. After excluding the void pixel, road overlaps on three of four pixels in its union, and car overlaps on one of two. The macro mean is 0.625.

## Input and scoring

Supply one UTF-8 CSV per mask, without headers. Rows run top to bottom, columns left to right. Both grids must have the same rectangular dimensions and spatial alignment. Labels are case-sensitive text with surrounding whitespace removed. The optional ignore value applies to reference pixels only. All other observed labels, including prediction-only classes, contribute equally to the mean.

The CLI in `mask_audit.py` opens both files and streams paired rows to `score`. It prints JSON with scored pixel count, intersections, unions and IoU. Invalid inputs exit with code 2. The synthetic masks live in `examples/` and unit checks in `tests/`.

## Operational scope

Use trusted local exports and limit input sizes when integrating into batch jobs. Nothing is sent over the network. This version evaluates one mask pair per invocation. Image decoding and dataset-wide aggregation are possible extensions. See CONTRIBUTING.md for changes, faq.md for input details and LICENSE for MIT terms.
