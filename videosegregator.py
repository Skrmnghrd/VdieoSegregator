import ffmpeg
import sys
import os
import shutil

"""
usage

python app.py souce/dir/where/to/startcrawling /dest/dir/to/move/allscreensaveers

"""
directories = []
list_of_files = []
screensaver_videos = []

source = str(sys.argv[1])
dest = str(sys.argv[2])



#walk dir and sub dirs as well
for root, subfiles, files in os.walk(source):
	for filename in files:
		fname = os.path.join(root, filename)
		list_of_files.append(fname)


#work with the videos
for files_name in list_of_files:
	if files_name.endswith('.mp4'):
		vid_width = ffmpeg.probe(files_name)["streams"][0]['width']
		vid_height = ffmpeg.probe(files_name)["streams"][0]['height']
		#print(str(vid_width) + 'x' + str(vid_height))

		if ((vid_width / vid_height) > 2.33 ): 
				#this means, its landscape with 9:21 aspect ratio

			if os.path.exists(os.path.join(dest, os.path.basename(files_name))) == False:
					#if it doesn't then copy it
				print("copying %s," % files_name)
				shutil.copy2(files_name,dest)
				shutil.copystat(files_name,dest)
			else:

				print("File:%s has a duplicate \nreanming..." % os.path.basename(files_name))
				i = 0 #iterator
				while True:
					i += 1
					new_filename = "{}{}".format( str(i),os.path.basename(files_name) )
					
					print("Projected filename:{}" .format(new_filename) )
					if os.path.exists(os.path.join(dest, new_filename)) == True:
						#if the file still exists skip and get new number
						continue
					else:
						
						shutil.copy2(files_name,(os.path.join(dest, new_filename)) )
						shutil.copystat(files_name,(os.path.join(dest, new_filename)) )
						break


					"""
					print(os.path.basename(files_name))
					print("OH!")
					os.path.basename(files_name) = "{}{}".format( 
						str(i),
						str(os.path.basename(files_name)[0])
						) 
					print(os.path.basename(files_name))
					"""


					#if os.path.exists(new_filename) == False:




