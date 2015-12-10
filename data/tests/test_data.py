""" Tests for checking the hashes for downloaded data
Run with:
    nosetests test_data.py
"""


from __future__ import print_function
from .. import manage_hashes

import tempfile

def test_check_hashes():
    with tempfile.NamedTemporaryFile() as temp:
        temp.write(b'Some data')
        temp.flush()
        fname = temp.name
        d = {fname: "5b82f8bf4df2bfb0e66ccaa7306fd024"}
        assert manage_hashes.check_hashes(d)
        d = {fname: "4b82f8bf4df2bfb0e66ccaa7306fd024"}
        assert not manage_hashes.check_hashes(d)
