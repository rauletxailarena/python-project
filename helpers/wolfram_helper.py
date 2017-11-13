import wolframalpha
from helpers.credentials import *

def ask_question():

    my_input = input("question: ")
    client = wolframalpha.Client(wolphram_app_id)
    print("Result:")
    result = client.query(my_input)
    if (next(result.results).text != None):
        answer = next(result.results).text
        print(answer)
    print ()

    print("Pods: ")
    for pod in result.pod:
        print(pod)
    print()


    print("Subpods: ")
    for pod in result.pods:
        for sub in pod.subpods:
            print(sub)
