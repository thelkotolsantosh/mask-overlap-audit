import unittest

from mask_audit import score


class MaskTests(unittest.TestCase):
    def test_asymmetric_overlap(self):
        result = score([["a", "a", "b"]], [["a", "b", "b"]])
        self.assertEqual(result["classes"]["a"], {"intersection": 1, "union": 2, "iou": 0.5})
        self.assertEqual(result["mean_iou"], 0.5)

    def test_prediction_only_class(self):
        self.assertEqual(score([["x"]], [["y"]])["classes"]["y"]["iou"], 0)

    def test_void(self):
        self.assertEqual(score([["void", "a"]], [["c", "a"]], "void")["mean_iou"], 1)

    def test_malformed(self):
        for a, b in [([], []), ([["x"]], []), ([["x"]], [["x", "x"]]),
                     ([["void"]], [["x"]]), ([[" "]], [["x"]])]:
            with self.subTest(a=a, b=b), self.assertRaises(ValueError):
                score(a, b, "void")
