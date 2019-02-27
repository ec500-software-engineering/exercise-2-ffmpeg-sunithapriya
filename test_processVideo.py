import pytest
from ffmpeg import processVideo
from pathlib import Path
import subprocess
from pytest import approx
import json

@pytest.fixture
def genpat(tmp_path) -> Path:
	"""
	generate test video
	"""
	vidfn = str(tmp_path / 'bars.avi')

	subprocess.check_call(['ffmpeg', '-v', 'warning', '-f', 'lavfi', '-i', 'smptebars', '-t', '5.', vidfn])
	return vidfn

def duration(path):
	return float(json.loads(subprocess.check_output(['ffprobe','-print_format','json','-show_format',path]))['format']['duration'])

def test_processVideo(genpat):

	fn = genpat
	result = processVideo(fn)

	orig_duration = duration(fn)
	duration_720 = duration(result[0])
	duration_480 = duration(result[1])

	assert orig_duration == approx(duration_720)
	assert orig_duration == approx(duration_480)




