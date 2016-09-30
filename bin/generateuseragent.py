"""ua to os - from a user agent return operating system, architecture, and browser"""

import sys,splunk.Intersplunk
import re

import unirest
import httplib
import urllib
import json
import ast

URI_PATH='https://useragentapi.com/api/v3/json/602950bd/'



def get_thing(line, path):
	response = unirest.get(path+""+urllib.quote_plus(line),headers={'Accept': 'application/json'})
	text=ast.literal_eval(json.dumps(response.body, ensure_ascii=False).encode('utf8'))
	try:
		text_data=text['data']
	except:
		text_data=text['error']
	return text_data
   

def get_ua_info(line):
	i = {}
	if "platform_name" in get_thing(line, URI_PATH):
		i['platform_name']= get_thing(line, URI_PATH)['platform_name']
	if "platform_version" in get_thing(line, URI_PATH):
		i['platform_version']= get_thing(line, URI_PATH)['platform_version']
	if "platform_type" in get_thing(line, URI_PATH):
		i['platform_type']= get_thing(line, URI_PATH)['platform_type']
	if "browser_name" in get_thing(line, URI_PATH):
		i['browser_name']= get_thing(line, URI_PATH)['browser_name']
	if "browser_version" in get_thing(line, URI_PATH):
		i['browser_version']= get_thing(line, URI_PATH)['browser_version']
	if "engine_name" in get_thing(line, URI_PATH):
		i['engine_name']= get_thing(line, URI_PATH)['engine_name']
	if "engine_version" in get_thing(line, URI_PATH):
		i['engine_version']= get_thing(line, URI_PATH)['engine_version']
	if "code" in get_thing(line, URI_PATH):
		i['platform_name']= ''
		i['platform_version']= ''
		i['platform_type']= ''
		i['browser_name']= ''
		i['browser_version']= ''
		i['engine_name']= ''
		i['engine_version']= ''
	return i

try:
    results,dummyresults,settings = splunk.Intersplunk.getOrganizedResults()
    for r in results:
        if "useragent" not in r:
            continue
        info = get_ua_info(r['useragent'])
        r.update(info)
except:
    import traceback
    stack =  traceback.format_exc()
    results = splunk.Intersplunk.generateErrorResults("Error : Traceback: " + str(stack))

splunk.Intersplunk.outputResults( results )