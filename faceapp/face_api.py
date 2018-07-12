import requests
from json import JSONDecoder
import csv

'''
********************************
alter image_file to image_base64
********************************
'''

http_detect_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
http_create_faceset_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create"
http_addface_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"
http_getfacetokenlist_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail"
http_search_url = "https://api-cn.faceplusplus.com/facepp/v3/search"
http_compare_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"


key ="6ljCt65MpiKzM0OW67Uf65KL_5NpcWrr"
secret ="_svrsgf9KQ2QGCHE5o2CG4ol74hFVPga"
faceset_outer_id = "test002"
formal_faceset_outer_id = "001"
test_csv_file_name = "face_token_name.csv"
'''
Mark Williams 'face_token': 'eb117fd4cbcc259bca2cc8d3eb0ca33f'
OSullivan '9a836d01b7e4b77498760ef203cecee1'
'''

def get_csv_dict(csvfilename):
	csvFile = open(csvfilename, "r")
	reader = csv.reader(csvFile)

	result = {}
	for item in reader:
		result[item[0]] = item[1]
	csvFile.close()
	return result

def get_name_with_facetoken(face_token):
	name_token_dict = get_csv_dict(test_csv_file_name)
	for token in name_token_dict:
		if face_token == token:
			return name_token_dict[token]
	return False 


def get_gender_and_age(img_base64):
	data = {"api_key":key, "api_secret": secret, "return_attributes": "gender,age"}

	# img_base64_file = {"image_base64": img_base64}
	# response = requests.post(http_detect_url, data=data, files=img_base64_file)
	data["image_base64"] = img_base64
	response = requests.post(http_detect_url, data=data)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)

	print(req_dict)
	if len(req_dict['faces']) == 0:
		return {'result':0, 'face_feat':[]}
	gender, age = (req_dict['faces'][0]['attributes']['gender']['value'], req_dict['faces'][0]['attributes']['age']['value'])
	return {'result':1, 'face_feat':[gender, age]}

def create_faceset(faceset_id):
	data = {"api_key":key, "api_secret":secret, "outer_id":faceset_id}

	response = requests.post(http_create_faceset_url, data)
	# req_con = response.content.decode('utf-8')
	# req_dict = JSONDecoder().decode(req_con)
	# print(req_dict.text)
	return response

def addface_to_faceset(img_base64, faceset_id, face_names):
	'''
	improvement: (require to) return the message requesting picture with more evident frontal face
	'''
	# if len(img_base64_batch) > 1:
	# 	print("Too many images!!!")
	# 	return 

	face_token_array = []
	face_token_str = ""

	data_for_detect = {"api_key":key, "api_secret": secret}
	# for img_base64 in img_base64_batch:
		# img_base64_file = {"image_base64": img_base64}
		# response = requests.post(http_detect_url, data=data_for_detect, files=img_base64_file)
	data_for_detect["image_base64"] = img_base64
	response = requests.post(http_detect_url, data=data_for_detect)
	print( response )
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)
	# print("req_dict:",req_dict)	

	if len( req_dict['faces'] ) > 1:
		return {"result":0, "errmsg":"require more evident frontal face picture!"}
	elif len( req_dict['faces'] ) == 0:
		return {"result":-1, "errmsg":"no face in pic"}

	# print(req_dict)
	# for face_info, limit in zip(req_dict['faces'], range(0, 5)):
	face_token_array.append( req_dict['faces'][0]['face_token'] )
	# print(face_token_array)

	face_token_str = req_dict['faces'][0]['face_token']
	# print(face_token_str)

	data_for_addface = {"api_key":key, "api_secret":secret, "outer_id":faceset_id, "face_tokens":face_token_str }
	response = requests.post(http_addface_url, data=data_for_addface)
	
	f = open(test_csv_file_name, 'a+', newline='')
	print( "face_token_arr:", len(face_token_array) )
	writer = csv.writer(f)
	for face_token, face_name in zip(face_token_array, face_names):
		facetoken_name_pair = []
		facetoken_name_pair.append(face_token)
		facetoken_name_pair.append(face_name)
		print("pairs to be written", facetoken_name_pair)
		writer.writerow(facetoken_name_pair)
	f.close()

	print(response.text)

	return {"result":1}

def compare_face(face_token1, face_token2):
	data = {"api_key":key, "api_secret": secret, "face_token1": face_token1, "face_token2":face_token2}
	response = requests.post(http_compare_url, data=data)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)
	print(req_dict)
	if req_dict['confidence'] > 80:
		return True
	else:
		return False
'''
def search_face(img_base64, faceset_id):
	stored_face_tokens = get_facetoken_list_from_faceset(faceset_id)

	# img_base64_file = {"image_file": img_base64}
	data = {"api_key":key, "api_secret": secret}
	data["image_base64"] = img_base64
	response = requests.post(http_detect_url, data=data)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)

	for face in req_dict['faces']:
		for stored_face_token in stored_face_tokens:
			if compare_face(face['face_token'], stored_face_token):
				name_token_pair_dict = get_csv_dict(test_csv_file_name)
				# print(name_token_pair_dict)
				return face['face_rectangle'], name_token_pair_dict[stored_face_token]

	msg = "No Match"
	# msg = False

	return msg
'''
def get_name_with_facetoken(face_token):
	name_token_dict = get_csv_dict(test_csv_file_name)
	for token in name_token_dict:
		if face_token == token:
			return name_token_dict[token]
	return False 

def search_all_face_in_img(img_base64, faceset_id):
	stored_face_tokens = get_facetoken_list_from_faceset(faceset_id)

	# img_base64_file = {"image_file": img_base64}
	data = {"api_key":key, "api_secret": secret}
	data["image_base64"] = img_base64
	response = requests.post(http_detect_url, data=data)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)
	if( len( req_dict['faces'] )  == 0):
		return {"result":-2,"errmsg":"no face in image"}	

	# name_token_pair_dict = get_csv_dict(test_csv_file_name)

	recognized_face_dict = []

	for face in req_dict['faces']:
		for stored_face_token in stored_face_tokens:
			# print( "face tokens from upload pic:", face )
			# print( "face tokens from stored pic:", stored_face_token )
			if compare_face(face['face_token'], stored_face_token):
				# recognized_face_dict[ face['face_token'] ] = (face['face_rectangle'], name_token_pair_dict[stored_face_token])
				name = get_name_with_facetoken(stored_face_token)
				if name:
					recognized_face_dict.append({"face_pos":face['face_rectangle'], "name":name})
				else:
					continue

				# print(name_token_pair_dict)
				# return face['face_rectangle'], name_token_pair_dict[stored_face_token]
	# print( "recognized_faces:", recognized_face_dict )
	if  len(recognized_face_dict) > 0:
		return {"result":1,"face_info":recognized_face_dict}
	else:
		msg = "No Match"
		# msg = False
		return {"result":-1,"errmsg":msg}

def search_face_with_name(img_base64, name, faceset_id):
	stored_face_tokens = get_facetoken_list_from_faceset(faceset_id)
	name_token_pair_dict = get_csv_dict(test_csv_file_name)
	face_token_of_name = ""

	for face_token in name_token_pair_dict:
		if name_token_pair_dict[face_token] == name:
			face_token_of_name = face_token
			break

	if len(face_token_of_name) == 0:
		msg = "name not in database"
		# msg = False
		return {"result":-2, "errmsg":msg}

	# img_base64_file = {"image_file": img_base64}
	data = {"api_key":key, "api_secret": secret}
	data["image_base64"] = img_base64
	response = requests.post(http_detect_url, data=data)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)
	
	if( len( req_dict['faces'] )  == 0):
		return {"result":-3,"errmsg":"no face in image"}

	# name_token_pair_dict = get_csv_dict(test_csv_file_name)

	recognized_face_dict = []

	for face in req_dict['faces']:
		if compare_face(face['face_token'], face_token_of_name):
			# recognized_face_dict[ face['face_token'] ] = (face['face_rectangle'], name_token_pair_dict[stored_face_token])
			recognized_face_dict.append( (face['face_rectangle'], name) )
			break	
			# print(name_token_pair_dict)
			# return face['face_rectangle'], name_token_pair_dict[stored_face_token]
	# print("recognized_face:", recognized_face_dict)
	if  len(recognized_face_dict) > 0:
		return {"result":1,"face_info":recognized_face_dict}
	else:
		msg = "No Match"
		# msg = False
		return {"result":-1,"errmsg":msg}

def get_name_list_from_faceset(faceset_id):
	'''
	data = {"api_key":key, "api_secret": secret, "outer_id": faceset_id}
	response = requests.post(http_getfacetokenlist_url, data=data)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)
	print( "req_dict", req_dict )	
	'''
	face_tokens_list = get_facetoken_list_from_faceset(faceset_id)
	face_name_list = []

	name_token_pair_dict = get_csv_dict(test_csv_file_name)
	# print(" name_token_pair:", name_token_pair_dict)
	for face_token1 in face_tokens_list:
		for face_token2 in name_token_pair_dict:
			if face_token1 == face_token2:			
				face_name_list.append( name_token_pair_dict[face_token2] )

	return list( set( face_name_list ) )

def get_facetoken_list_from_faceset(faceset_id):
	data = {"api_key":key, "api_secret": secret, "outer_id": faceset_id}
	response = requests.post(http_getfacetokenlist_url, data=data)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)
	# print( "req_dict", req_dict )

	face_tokens_list = req_dict['face_tokens']
	return face_tokens_list      











