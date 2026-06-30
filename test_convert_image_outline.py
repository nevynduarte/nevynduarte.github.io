"""
Regression tests for convert_image_outline.py

Covers the bug where batch_process_logos() reported len(image_files) as the
number of processed logos even though already-converted outputs (files ending
in -white-purple.png) are explicitly skipped in the loop, causing the summary
to overcount on every re-run.
"""
import unittest
from unittest.mock import patch, MagicMock

import convert_image_outline


class TestBatchProcessLogosCount(unittest.TestCase):

    def _run_batch(self, listdir_return):
        """Run batch_process_logos with a mocked filesystem, suppressing output."""
        with patch('os.path.exists', return_value=True), \
             patch('os.listdir', return_value=listdir_return), \
             patch('convert_image_outline.process_image') as mock_process, \
             patch('builtins.print'):
            mock_process.return_value = MagicMock()
            count = convert_image_outline.batch_process_logos()
        return count, mock_process

    def test_skips_already_converted_outputs(self):
        """Count must exclude files that end with -white-purple.png (previous run outputs)."""
        count, mock_process = self._run_batch([
            'logo1.png',
            'logo2.png',
            'logo1-white-purple.png',   # already-processed output — must be skipped
        ])

        self.assertEqual(count, 2)
        self.assertEqual(mock_process.call_count, 2)

    def test_skips_double_processed_outputs(self):
        """Files ending in -white-purple-white-purple.png must also be skipped."""
        count, mock_process = self._run_batch([
            'logo1.png',
            'logo1-white-purple.png',
            'logo1-white-purple-white-purple.png',
        ])

        self.assertEqual(count, 1)
        self.assertEqual(mock_process.call_count, 1)

    def test_all_already_converted_returns_zero(self):
        """Returns 0 and calls process_image 0 times when every file is a prior output."""
        count, mock_process = self._run_batch([
            'logo1-white-purple.png',
            'logo2-white-purple.png',
        ])

        self.assertEqual(count, 0)
        mock_process.assert_not_called()

    def test_no_outputs_present_processes_all(self):
        """When no prior outputs exist, every image file is processed."""
        count, mock_process = self._run_batch([
            'alpha.png',
            'beta.jpg',
            'gamma.jpeg',
        ])

        self.assertEqual(count, 3)
        self.assertEqual(mock_process.call_count, 3)

    def test_missing_directory_returns_zero(self):
        """Returns 0 immediately when the logos directory does not exist."""
        with patch('os.path.exists', return_value=False), \
             patch('builtins.print'):
            count = convert_image_outline.batch_process_logos()

        self.assertEqual(count, 0)

    def test_empty_directory_returns_zero(self):
        """Returns 0 when the directory exists but contains no image files."""
        with patch('os.path.exists', return_value=True), \
             patch('os.listdir', return_value=['readme.txt']), \
             patch('builtins.print'):
            count = convert_image_outline.batch_process_logos()

        self.assertEqual(count, 0)

    def test_failed_process_not_counted(self):
        """A file that raises an exception during process_image is not counted."""
        with patch('os.path.exists', return_value=True), \
             patch('os.listdir', return_value=['good.png', 'bad.png']), \
             patch('convert_image_outline.process_image') as mock_process, \
             patch('builtins.print'):
            # First call succeeds, second raises
            mock_process.side_effect = [MagicMock(), RuntimeError('disk full')]
            count = convert_image_outline.batch_process_logos()

        self.assertEqual(count, 1)


if __name__ == '__main__':
    unittest.main()
