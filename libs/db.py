#!/usr/bin/env python3
#-*- coding:utf-8 -*-  

############################
# Usage:
# File Name: db.py
# Author: annhe  
# Mail: i@annhe.net
# Created Time: 2015-12-10 12:08:37
############################

import json
import sys
import fcntl

def init_DB(file_db):
	try:
		with open(file_db, 'r') as f:
			db = json.load(f)
	except:
		db = {}
	return(db)

def updateDB(file_db, msg):
	db = init_DB(file_db)
	if not db:
		data = msg
	else:
		namelist = db['名称'].split(",")
		if msg['名称'] not in namelist:
			namelist.append(msg['名称'])
		db['名称'] = ",".join(namelist)
		try:
			db['eventid'] = db['eventid'] + "," + msg['eventid']
		except:
			pass
#		if db['名称'] != msg['名称']:
#			db['名称'] = db['名称'] + "," + msg['名称']
		if "IP" in msg and "IP" in db:
			if db['IP'] != msg['IP']:
				db['IP'] = db['IP'] + "," + msg['IP']
		db['数据'] = db['数据'] + msg['数据']
		data = db

	with open(file_db, 'w') as f:
		fcntl.flock(f, fcntl.LOCK_EX)
		json.dump(data, f, ensure_ascii=False)
		fcntl.flock(f, fcntl.LOCK_UN)

if __name__ == '__main__':
	updateDB(sys.argv[1], json.loads(sys.argv[2]))
	#print(init_DB(sys.argv[1]))
