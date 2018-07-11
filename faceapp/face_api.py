import requests
from json import JSONDecoder

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

def get_gender_and_age(img_base64):
	data = {"api_key":key, "api_secret": secret, "return_attributes": "gender,age"}

	# img_base64_file = {"image_base64": img_base64}
	# response = requests.post(http_detect_url, data=data, files=img_base64_file)
	data["image_base64"] = img_base64
	response = requests.post(http_detect_url, data=data)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)

	print(req_dict)
	gender, age = (req_dict['faces'][0]['attributes']['gender']['value'], req_dict['faces'][0]['attributes']['age']['value'])
	return (gender, age)

def create_faceset(faceset_id):
	data = {"api_key":key, "api_secret":secret, "outer_id":faceset_id}

	response = requests.post(http_create_faceset_url, data)
	# req_con = response.content.decode('utf-8')
	# req_dict = JSONDecoder().decode(req_con)
	# print(req_dict.text)
	return response

def addface_to_faceset(img_base64, faceset_id, face_name):
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
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)

	if len( req_dict['faces'] ) > 1:
		print("Please upload more evident frontal face picture!")
		return False

	# print(req_dict)
	# for face_info, limit in zip(req_dict['faces'], range(0, 5)):
	# face_token_array.append( req_dict['faces'][0]['face_token'] )
	# print(face_token_array)

	face_token_str = req_dict['faces'][0]['face_token']
	print(face_token_str)

	data_for_addface = {"api_key":key, "api_secret":secret, "outer_id":faceset_id, "face_tokens":face_token_str }
	response = requests.post(http_addface_url, data=data_for_addface)

	f = open(test_csv_file_name, 'a+', newline='')
	writer = csv.writer(f)
	for face_token, face_name in zip(face_token_array, face_names):
		facetoken_name_pair = []
		facetoken_name_pair.append(face_token)
		facetoken_name_pair.append(face_name)
		# print(facetoken_name_pair)
		writer.writerow(facetoken_name_pair)
	f.close()

	print(response.text)

	return

def compare_face(face_token1, face_token2):
	data = {"api_key":key, "api_secret": secret, "face_token1": face_token1, "face_token2":face_token2}
	response = requests.post(http_compare_url, data=data)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)
	# print(req_dict)
	if req_dict['confidence'] > 80:
		return True
	else:
		return False

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

def get_facetoken_list_from_faceset(faceset_id):
	data = {"api_key":key, "api_secret": secret, "outer_id": faceset_id}
	response = requests.post(http_getfacetokenlist_url, data=data)
	req_con = response.content.decode('utf-8')
	req_dict = JSONDecoder().decode(req_con)

	face_tokens_list = req_dict['face_tokens']
	face_name_list = []

	name_token_pair_dict = get_csv_dict(test_csv_file_name)

	for face_token1 in req_dict['faces']:
		for face_token2 in name_token_pair_dict:
			if face_token1 == face_token2:			
				face_name_list.append( name_token_pair_dict[face_token2] )

	return face_name_list












