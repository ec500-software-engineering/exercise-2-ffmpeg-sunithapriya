import os
import subprocess
import Queue
import threading 


threads = []
def processVideo(filename):
	print("Processing"+filename)
	if filename+"_720p.mp4" in os.listdir("outputVideos"):
		os.remove("outputVideos/"+filename+"_720p.mp4")
	if filename+"_480p.mp4" in os.listdir("outputVideos"):
		os.remove("outputVideos/"+filename+"_480p.mp4")

	subprocess.call("ffmpeg -loglevel panic -i inputVideos/"+filename+" -vf scale=-1:720 -b:v 2097152 -r 30 outputVideos/"+filename+"_720p.mp4",shell=True)
 	print("Processed"+filename+" to 720p")
 	subprocess.call("ffmpeg -loglevel panic -i inputVideos/"+filename+" -vf scale=-1:480 -b:v 1048576 -r 30 outputVideos/"+filename+"_480p.mp4", shell=True)
 	print("Processed"+filename+" to 480p")


video_types = ['.avi','.AVI','.wmv','.WMV','.mpg','.MPG','.mpeg','.MPEG','.mp4']
q = Queue.Queue()

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


