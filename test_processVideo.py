import pytest
from ffmpeg import processVideo
from pathlib import Path
import subprocess
import myffmpeg

@pytest.fixture
def genpat(tmp_path) -> Path:
	"""
	generate test video
	"""
	vidfn = tmp_path / 'bars.avi'

	subprocess.check_call(['ffmpeg', '-v', 'warning', '-f', 'lavfi', '-i', 'smptebars', '-t', '5.', str(vidfn)])
	return vidfn

def test_processVideo(genpat):

	fn = genpat
	result = processVideo(fn)