import sys
sys.path.append('..')

import us.counties as usc

def test_name():
    assert usc.county_file_name('New Jersey') == 'data/counties/new-jersey.csv'