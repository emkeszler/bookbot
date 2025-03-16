from stats import word_count,char_count, sort_dicts
import sys

def main():
	if len(sys.argv) > 1:	
		frank_path = sys.argv[1]
		print("============ BOOKBOT ============")
		print("Analyzing book found at", frank_path, "...")
		print("----------- Word Count ----------")
		with open(frank_path) as f:
			print("Found",word_count(f), "total words")
			print("--------- Character Count -------")
		with open(frank_path) as f:
			char_dict = char_count(f)
		sorted_chars = sort_dicts(char_dict)
		for sort in sorted_chars:
			if sort[0].isalpha():
				print(f"{sort[0]}: {sort[1]}")
		print("============= END ===============")
	else: 
		sys.exit("Usage: python3 main.py <path_to_book>")
#raise Exception("Usage: python3 main.py <path_to_book>")
def get_book_text(path):
	with open(path) as f:
		return f.read()
try:
	main()
except Exception as e:
	print(e)

