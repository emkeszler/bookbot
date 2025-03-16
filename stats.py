def word_count(text):
        book = text.read()
        indiv_words=book.split()
        len_txt = len(indiv_words)
        return len_txt

def char_count(text):
	book = text.read()
	char_dict = {} 
	for char in book:
		s = char.lower()
		if s in char_dict:
			char_dict[s] += 1
		else:
			char_dict[s]=1
	return char_dict	
	
def sort_dicts(unsorted_dict):
	sorted_dict = sorted(unsorted_dict.items(), reverse=True,key=lambda item: item[1])
	return(sorted_dict)
