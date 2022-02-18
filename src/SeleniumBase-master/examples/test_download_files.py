import math
from seleniumbase import BaseCase


class DownloadTests(BaseCase):

    def test_download_files(self):
        self.open("https://pypi.org/project/seleniumbase/#files")
        pkg_header = self.get_text("h1.package-header__name").strip()
        pkg_name = pkg_header.replace(" ", "-")
        whl_file = pkg_name + "-py2.py3-none-any.whl"
        tar_gz_file = pkg_name + ".tar.gz"

        # Click the links to download the files into: "./downloaded_files/"
        # (If using Safari, IE, or Chromium Guest Mode: download directly.)
        # (The default Downloads Folder can't be changed when using those.)
        whl_selector = 'div#files a[href$="%s"]' % whl_file
        tar_selector = 'div#files a[href$="%s"]' % tar_gz_file
        if self.browser == "safari" or self.browser == "ie" or (
                self.is_chromium() and self.guest_mode and not self.headless):
            whl_href = self.get_attribute(whl_selector, "href")
            tar_href = self.get_attribute(tar_selector, "href")
            self.download_file(whl_href)
            self.download_file(tar_href)
        else:
            self.click(whl_selector)
            self.click(tar_selector)

        # Verify that the downloaded files appear in the [Downloads Folder]
        # (This only guarantees that the exact file name is in the folder.)
        # (This does not guarantee that the downloaded files are complete.)
        # (Later, we'll check that the files were downloaded successfully.)
        self.assert_downloaded_file(whl_file)
        self.assert_downloaded_file(tar_gz_file)

        self.sleep(1)  # Add more time to make sure downloads have completed

        # Get the actual size of the downloaded files (in bytes)
        whl_path = self.get_path_of_downloaded_file(whl_file)
        with open(whl_path, 'rb') as f:
            whl_file_bytes = len(f.read())
        print("\n%s | Download = %s bytes." % (whl_file, whl_file_bytes))
        tar_gz_path = self.get_path_of_downloaded_file(tar_gz_file)
        with open(tar_gz_path, 'rb') as f:
            tar_gz_file_bytes = len(f.read())
        print("%s | Download = %s bytes." % (tar_gz_file, tar_gz_file_bytes))

        # Check to make sure the downloaded files are not empty or too small
        self.assert_true(whl_file_bytes > 5000)
        self.assert_true(tar_gz_file_bytes > 5000)

        # Get file sizes in kB to compare actual values with displayed values
        whl_file_kb = whl_file_bytes / 1000.0
        whl_line = self.get_text("tbody tr:nth-of-type(1) th")
        whl_displayed_kb = float(whl_line.split("(")[1].split(" ")[0])
        tar_gz_file_kb = tar_gz_file_bytes / 1000.0
        tar_gz_line = self.get_text("tbody tr:nth-of-type(2) th")
        tar_gz_displayed_kb = float(tar_gz_line.split("(")[1].split(" ")[0])

        # Verify downloaded files are the correct size (account for rounding)
        self.assert_true(abs(
            math.floor(whl_file_kb) - math.floor(whl_displayed_kb)) < 2)
        self.assert_true(abs(
            math.floor(tar_gz_file_kb) - math.floor(tar_gz_displayed_kb)) < 2)
