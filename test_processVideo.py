import pytest
from ffmpeg import processVideo
from pathlib import Path
import subprocess
from pytest import approx
import json

#@pytest.fixture
# def genpat(tmp_path) -> Path:
# 	"""
# 	generate test video
# 	"""
# 	vidfn = str(tmp_path / 'bars.avi')

# 	subprocess.check_call(['ffmpeg', '-v', 'warning', '-f', 'lavfi', '-i', 'smptebars', '-t', '5.', vidfn])
# 	return vidfn

def get_duration(file):
    """Get the duration of a video using ffprobe."""
    cmd = 'ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(file)
    output = subprocess.check_output(
        cmd,
        shell=True, # Let this run in the shell
        stderr=subprocess.STDOUT
    )
    # return round(float(output))  # ugly, but rounds your seconds up or down
    return float(output)

# def getLength(input_video):
# 	result = subprocess.Popen('ffprobe -i input_video -show_entries format=duration -v quiet -of csv="p=0"', stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
# 	output = result.communicate()
# 	return output[0]

# def duration(path):
# 	return float(json.loads(subprocess.check_output("ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 video2.mp4")))

def test_processVideo():

	fn = 'video2.mp4'
	result = processVideo(fn)

	orig_duration = get_duration(fn)
	duration_720 = get_duration(result[0])
	duration_480 = get_duration(result[1])

	assert orig_duration == duration_720
	assert orig_duration == duration_480




