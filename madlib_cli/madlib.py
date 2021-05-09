import regex


def intro():
    print("""
    |-------------------------------------------------------------------|
    |                              Welcome                              |
    |-------------------------------------------------------------------|
    Madlib is a game where you enter words of the type i ask and then 
    i'll comine those words to form a charachter in video game based on
    your inputs.
    Ready? GO~>
    """)


def read_template(path:str)->str:
    """
    takes in a path to text file and returns a stripped string of the file’s contents.
    read_template should raise a FileNotFoundError if path is invalid.
    """
    try:
        with open(path,'r') as file:
            read_data = file.read().replace('\n','')
            return read_data
    except: raise FileNotFoundError

def parse_template(template:str):
    """
    takes in a template string
    returns a string with language parts removed
    and 
    returns a separate list of those language parts.
    """
    parts_list =regex.findall('\{(.*?)\}',template)
    # https://stackoverflow.com/questions/51051136/extracting-content-between-curly-braces-in-python
    parts_tup = tuple(parts_list)
    stripped = regex.sub('\{(.*?)\}','{}',template)
    # https://stackoverflow.com/questions/11844986/convert-or-unformat-a-string-to-variables-like-format-but-in-reverse-in-p
    return stripped, parts_tup


def merge(bare_template:str, user_list:list):
    """
    takes in a “bare” template and a list of user entered language parts
    returns a string with the language parts inserted into the template. 
    """
    return bare_template.format(*user_list)


def save_in_a_file(data:str):
    """
    Write the completed text to a new file on your file system 
    """
    path = 'assets/your_output.txt'
    try:
        with open(path,'w') as file:
            write_data = file.write(data)
            print(f'\n**saved successfully**\nfile path:{path}\nBye:)\n')
    except: raise FileNotSaved

def main():
    user_inputs = []
    intro()
    template = read_template('assets/make_me_a_video_game_template.txt')
    stripped, parts=parse_template(template)
    for word in parts:
        user_inputs.append(input(f'> {word} ? '))
    output = merge(stripped,user_inputs)
    print('\n'+output)
    save_in_a_file(output)
    
if __name__ == "__main__":
    main()

    