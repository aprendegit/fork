def are_items_equal(list_of_images_expected, list_of_images_obtained):
	""" Receive two lists and compare if the images are the same in both lists.
		To make this comparison it uses the full name of the images contains in  the lists
		
		Key parameters:
		list_of_images_expected -- A list that contains ImageFile objects
		list_of_images_obtained -- A list that contains ImageFile objects 
		
		Return:
		result_and_message -- A list that will contain the boolean value and a message
							The boolean value will be stored in the first position and the message, 
							that contains the reason for failure or success will be stored in 
							the second position.
	
	"""
	are_equal = True
	message = ""
	if len(list_of_images_expected) == len(list_of_images_obtained):
		for image_object in list_of_images_obtained:
			if image_object.get_complete_image_with_type() not in list_of_images_expected:
				are_equal = False	
				message = "Not equal. " + image_object.get_complete_image_with_type() + " \
							not in " + ', '.join(list_of_images_expected)
	else:
		are_equal = False
		message = "Not equal. The length of lists is different"
	result_and_message = [are_equal, message]
	return result_and_message
	
def is_item_in_list(item, list_of_images_obtained):
	""" Verify if the FileImage item given is contained in the list of ImageFile objects 
		
		Key parameters:
		item -- An ImageFile object
		list_of_images_obtained -- A list of ImageFile objects 
		
		Return:
		result_and_message -- A list that will contain a bolean value and a message.
							The boolean value will be stored in the first position and the message, 
							that contains the reason for failure or success will be stored in 
							the second position.
	
	"""
	is_item_in_list = False
	message = "Item is not there. "
	for image_object in list_of_images_obtained:
		if item.get_complete_image_with_type() == image_object.get_complete_image_with_type():
			is_item_in_list = True
			message = "Item is there."
	result_and_message = [is_item_in_list, message]
	return result_and_message