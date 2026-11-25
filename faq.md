# FAQ

## 1. What does this tool compare?

A reference segmentation mask and a predicted mask for the same image.

## 2. Why inspect individual classes?

A small foreground object can have low overlap even when most background pixels match.

## 3. What is the main metric?

Intersection over union measures how much the two regions for a label overlap.

## 4. Which summaries are included?

Each label has its intersection, union and IoU, alongside the overall scored pixel count and macro mean.

## 5. Which language is used?

Python implements the row reader, scoring function and command line.

## 6. Which libraries are required?

The csv, collections, itertools, argparse and json modules ship with Python.

## 7. What runtime should I use?

Use Python 3.10 or later with read access to both input files.

## 8. How do I install it?

Download the repository and open its directory. No package installation is needed.

## 9. How do I configure void pixels?

Pass --ignore void if the reference uses the literal label void.

## 10. How do I run the sample?

Run python mask_audit.py examples/reference.csv examples/prediction.csv --ignore void.

## 11. Where is the implementation?

mask_audit.py contains the scorer and CLI. The examples directory contains a matching pair of grids.

## 12. How is union calculated?

Add the reference and prediction counts for a label, then subtract its intersection.

## 13. Which file format works?

Use headerless UTF-8 CSV with one row per scanline and one class label per cell.

## 14. How do I save the report?

Redirect standard output to a JSON file after checking the command exit status.

## 15. Can I use numeric classes?

Yes. IDs are treated as text, so 01 and 1 are distinct labels.

## 16. What happens on invalid data?

An empty label, incompatible shape or absence of scored pixels produces an error and exit code 2.

## 17. Why does a header appear in my scores?

A header looks like an ordinary row of labels. Remove it from both exports.

## 18. Why might matching shapes still score poorly?

Confirm that orientation, crop and label mappings agree between exports.

## 19. How do I test the scorer?

Run python -m unittest discover -s tests -v from the project root.

## 20. How should I contribute a scoring change?

Include a tiny input and its hand-calculated expected result as a regression test.

## 21. Can it read PNG masks directly?

Export class IDs to CSV first and preserve the original resolution.

## 22. Can it run in a batch pipeline?

Process one aligned pair per call, capture its exit status and retain the JSON for successful pairs.

## 23. How could dataset aggregation be added?

Accumulate intersections and unions across images for each class before dividing.

## 24. What data leaves the machine?

The CLI reads local files and writes to stdout. Protect exported labels and reports using filesystem permissions.

## 25. Where is the sample calculation explained?

The README walks through the road and car scores in the bundled example.
