from datetime import date, datetime

def makeScript(shipName="ORBIT", beginDate=date.today().year):
	script = [
	'{\n',
		'time{utc "2015-01-01T00:01:24.0000"}\n',
		'select{object "Orbit-test-spacecraft"}\n',
		'center {time 5.0}\n',
		'goto { time 5.0 }\n',
		'follow{}\n',
		'lock{}\n',
	'}'
	]
	#set new begin date
	if (beginDate==date.today().year): #case when begin param default
		script[1] = 'time{utc "' + str(beginDate) +'-01-01T00:01:24.0000'+'"}\n'
	else:
		script[1] = 'time{utc "' + str(beginDate) + '"}\n'

	#set new ship object
	script[2] = 'select{object "' + str(shipName) + '"}\n'

	f = open("script.cel","w")	
	for line in script:
		f.write(line)
	return script

def makeSSCScript(shipName="ORBIT",beginDate=date.today().year, endDate=date.today().year+1):
	scriptSSC = [
	'"Orbit-test-spacecraft" "Sol"\n',
	'{\n',
		'\tClass "spacecraft"\n',
		'\tMesh "orbit.3ds"\n',
		'\tRadius 0.011\n',
		'\tOrientation [ 180 1 0 0 ]\n',
		'\tTimeline [\n',
		'\t# Phase 3: Solstice mission\n',
	'\t{\n',
		'\tBeginning "2015 01 01 00:00:00"\n',
		'\tEnding    "2020  9 15 17:02:00"\n',
		'\tOrbitFrame { EclipticJ2000 { Center "Sol/Earth" } }\n',
		'\tSampledTrajectory { Source "orbit.xyzv" }\n',
	'\t}\n',
	'\t]\n',
	'}\n',
	]
	#set new ship name
	scriptSSC[0] = '"'+str(shipName)+'" "Sol"\n'
	#set new begin/end date

	#when end/begin default
	if (beginDate == date.today().year and endDate == beginDate+1):
		scriptSSC[9] = '\tBeginning "' +str(beginDate)+'-01-01T00:01:24.0000"\n'
		scriptSSC[10] = '\tEnding "' +str(endDate)+'-01-01T00:01:24.0000"\n'
	else:
		scriptSSC[9] = '\tBeginning "' +str(beginDate)+'"\n'
		scriptSSC[10] = '\tEnding "' +str(endDate)+'"\n'

	f = open("orbit.ssc","w")	
	for line in scriptSSC:
		f.write(line)
	return scriptSSC

if __name__ == '__main__':
	makeScript() #return default script
	makeSSCScript() #return default ssc script

	#and some custom scripts
	makeSSCScript(beginDate="2015 01 01 00:00:00",endDate="2016 01 01 00:00:00",shipName="ORBIT")
	makeScript(beginDate="2023 02 03 00:00:00")
	makeScript(shipName="Orbital battlestation Death Star I")