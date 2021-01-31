import requests
import os

# html_a = requests.get("https://gist.github.com/serranoarevalo/a830deafa1dc133b8f4e6ee19e56d0be")
# print(html_a.text)

# print(html_a.status_code)

print("Welcome to IsItDown.py!")
print("Please write a URL or URLs you want to check. (separated by comma)")

repeat = ""

while True:
    input_urls = input().lower().split(',')
    
    
    repeat = input("Do you want to start over? y/n ").lower()

    if repeat == "y":
        print("repeat!")
        # print(input_urls.strip(repeat))
    elif repeat == "n":
        break
    else:
        print("That's not a valid answer.")
        break

# urls = input().lower()
# user_urls = urls.strip()

# for user_urls in urls:
#     repeat = input("Do you want to start over? y/n ").lower()

#     if repeat == "y":
#         print("repeat!")
#     elif repeat == "n":
#         break
#     else:
#         print("That's not a valid answer.")
#         break