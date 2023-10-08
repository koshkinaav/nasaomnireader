import datetime
import os

from nasaomnireader.nasaomnireader import omnireader


def test_omnireader_can_download_txt():
    """
    Test that we can get to the omni FTP location
    for text files and that
    we have a sane local directory for storing files
    """
    dt = datetime.datetime(2005, 1, 1)
    od = omnireader.omni_downloader(cdf_or_txt='txt', force_download=True)
    fakecdf = od.get_cdf(dt, '5min')
    downloaded_txt = os.path.join(od.localdir, od.filename_gen['5min'](dt))
    assert os.path.exists(downloaded_txt)

test_omnireader_can_download_txt()