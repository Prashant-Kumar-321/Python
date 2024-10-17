import emoji
import sys


def main(): 
    print("Print Emoji:")

    user_input = input("Enter Prompt: ")
    for_emoji = get_formated_str(user_input)
    emoji_code = emoji.emojize(for_emoji, language='alias')

    if not emoji.is_emoji(emoji_code): 
        sys.exit("Emoji Not found")

    print(emoji_code) 


def get_formated_str(emoji_str): 
    return f":{concat(emoji_str)}:"

def concat(user_prompt): 
    comps = user_prompt.strip().split(' ')

    result = ""
    for i in range(len(comps)): 
        if i == 0: 
            result = comps[i]
            continue 
        result += "_" + comps[i]
    
    return result
        
def test1(): 
    user_prompt = "man gesturing ok"
    # expected output = man_gesturing_ok
    if concat(user_prompt) == "man_gesturing_ok": 
        print("test passed")
    else: 
        print("test failed")
    # print(concat(user_prompt))
    # print("abcabcde".lstrip("ab"))

if __name__ == '__main__': 
    main() 
