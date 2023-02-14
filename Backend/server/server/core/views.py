from django.http import JsonResponse


def is_palindrome(request, word):
    is_palindrom = word == word[::-1]
    middle = None
    if len(word) % 2 == 1:
        middle = word[len(word) // 2]

    if is_palindrom and middle:
        return JsonResponse({
            "message": f"The input '{word}' is a palindrome and its middle letter is '{middle}'."
        })

    return JsonResponse({
        "message": f"The input '{word}' is not a palindrome."
    })
