import os
import os.path
import subprocess
import queue
import threading 

def processVideo(file):
	filename,ext= os.path.splitext(file)
	print("Processing"+filename)
	if os.path.isfile(filename+"_720p.mp4"):
		os.remove(filename+"_720p.mp4")
	if os.path.isfile(filename+"_480p.mp4"):
		os.remove(filename+"_480p.mp4")
	# if filename+"_720p.mp4" in os.listdir("outputVideos"):
	# 	os.remove("outputVideos/"+filename+"_720p.mp4")
	# if filename+"_480p.mp4" in os.listdir("outputVideos"):
	# 	os.remove("outputVideos/"+filename+"_480p.mp4")

	subprocess.call("ffmpeg -loglevel warning  -i "+file+" -vf scale=1280:720 -b:v 2M "+filename+"_720p.mp4",shell=True)
	print("Processed",file," to 720p")
	subprocess.call("ffmpeg -loglevel warning -i "+file+" -vf scale=640:480 -b:v 1M "+filename+"_480p.mp4", shell=True)
	print("Processed",file," to 480p")
	output=[filename+"_720p.mp4",filename+"_480p.mp4"]
	return output

if __name__=="__main__":
	threads = []
	video_types = ['.avi','.AVI','.wmv','.WMV','.mpg','.MPG','.mpeg','.MPEG','.mp4']
	q = queue.Queue()


	for file in os.listdir("inputVideos"):
		filename,ext= os.path.splitext(file)
		if ext in video_types:
			q.put(file)

	while not q.empty():
		filename = q.get()
		t = threading.Thread(target=processVideo, args = (filename,))
		threads.append(t)
		t.daemon = True
		t.start()

	for thread in threads:
		thread.join()


