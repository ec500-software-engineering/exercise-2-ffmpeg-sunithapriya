import os
import subprocess
import Queue
import threading 

# for filename in os.listdir("inputVideos"):
# 	print(filename)
# 	if (filename.endswith(".mp4")):
# 		subprocess.call("ffmpeg -i inputVideos/"+filename+" -vf scale=-1:720 -b:v 2097152 -r 30 outputVideos/"+filename+"_720p.mp4",shell=True)
# 		subprocess.call("ffmpeg -i inputVideos/"+filename+" -vf scale=-1:480 -b:v 1048576 -r 30 outputVideos/"+filename+"_480p.mp4", shell=True)
# 	else:
# 		continue

threads = []

def convertVideo720(filename):
	print("Converting "+filename+" to 720p")
	if filename+"_720p.mp4" in os.listdir("outputVideos"):
		os.remove("outputVideos/"+filename+"_720p.mp4")
	result = subprocess.check_output("ffmpeg  -loglevel panic -i inputVideos/"+filename+" -vf scale=-1:720 -b:v 2097152 -r 30 outputVideos/"+filename+"_720p.mp4",shell=True)
	print("Converted "+filename+" to 720p")	

def convertVideo480(filename):
	print("Converting "+filename+" to 480p")
	if filename+"_480p.mp4" in os.listdir("outputVideos"):
		os.remove("outputVideos/"+filename+"_480p.mp4")
	subprocess.check_output("ffmpeg -loglevel panic -i inputVideos/"+filename+" -vf scale=-1:480 -b:v 1048576 -r 30 outputVideos/"+filename+"_480p.mp4", shell=True)
	print("Converted "+filename+" to 480p")

def processVideo(filename):
	t1 = threading.Thread(target=convertVideo720, args = (filename,))
	t2 = threading.Thread(target=convertVideo480, args = (filename,))
	t1.daemon = True
	t2.daemon = True
	threads.append(t1)
	threads.append(t2)
	t1.start()
	t2.start()

video_types = ['.avi','.AVI','.wmv','.WMV','.mpg','.MPG','.mpeg','.MPEG','.mp4']
q = Queue.Queue()

for file in os.listdir("inputVideos"):
	filename,ext= os.path.splitext(file)
	if ext in video_types:
		q.put(file)

while not q.empty():
	filename = q.get()
	print("Processing "+filename)
	processVideo(filename)

for thread in threads:
	thread.join()

