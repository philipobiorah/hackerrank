import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    result = ""
    word_list = wrapper.wrap(text=string)
	
    for element in word_list:
            result = result + element + "\n"
    return result	
    


if __name__ == '__main__':
      string, max_width = input(), int(input())
      result = wrap(string, max_width)
      print(result)