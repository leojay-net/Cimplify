import openai
from decouple import config
import json
from openai import OpenAI


def get_response(problem, aoc="generally"):
    client = OpenAI(
        api_key=config("OPENAI_API_KEY")
    )


    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": "You are a helpful tutor assistant for different subjects, You are to give detailed, broken down to easy step by step solutions to any given problem with detailed examples provided the problem is wiithin the constraint of eduction on books, schhools, topics. You are speaking to students who needs to learn so speak gently"},
        {"role": "user", "content": "I am need of detailed explanation, step-by-step on the following 'I'm having difficulty understanding how to find the derivative of a function' and I have been trying to study it but don't quite get a hang of it "+". I would love for the answer to be from the following context 'calculus'. Can you explain it for me?"},
        {"role": "assistant", "content": "Certainly! To find the derivative of a function\
            f(x)\
            f(x), follow these steps:\
            Identify the function: Let f(x) be the given function. Use power rule: For a term\
            ax^n, the derivative is n⋅ax^(n-1).\
            Sum rule: If\
            f(x)=g(x)+h(x), then f'(x)=g'(x)+h'(x).\
            Product rule: If f(x)=g(x)⋅h(x), then f'(x)=g'(x)⋅h(x)+g(x)⋅h'(x).\
            Chain rule: If f(x)=g(h(x)), then f'(x)=g'(h(x))⋅h'(x).\
            "},
        {"role": "user", "content": "I am need of detailed explanation, step-by-step on the following 'How do I find the area of a circle' and I have been trying to study it but don't quite get a hang of it "+". I would love for the answer to be from the following context 'generally'. Can you explain it for me?"},
        {"role": "assistant", "content": "The area of a circle is the amount of space inside the circle. To find the area of a circle, you need to know the radius of the circle, which is the distance from the center of the circle to any point on the circle. The formula for the area of a circle is:\
            A=πr2\
            where A is the area, π is a constant that is approximately equal to 3.14, and r is the radius. To use the formula, you need to follow these steps:\
            Plug in the value of the radius into the formula. For example, if the radius is 5 cm, then the formula becomes:\
            A=π(5)2\
            Simplify the expression by performing the operations inside the parentheses. For example, (5)2 is equal to 25, so the formula becomes:\
            A=π(25)\
            Multiply the value of π by the value inside the parentheses. For example, π(25) is equal to 78.5, so the formula becomes:\
            A=78.5\
            Write the answer with the appropriate unit of measurement. For example, if the radius was given in centimeters, then the area should also be in square centimeters, so the answer is:\
            A=78.5 cm2\
            "},
        {"role": "user", "content": "I am need of detailed explanation, step-by-step on the following "+ str(problem).replace('"', "'")+" and I have been trying to study it but don't quite get a hang of it "+". I would love for the answer to be from the following context "+str(aoc).replace('"', "'")+". Can you explain it for me?"}
    ],
    #response_format={"type": "json_object"},
    temperature=0.7,
        max_tokens=700,
        n=1,
        stop=None
    )
    obj = response.choices[0].message.content
    return obj

    

# result = get_response(problem="I'm struggling to balance chemical equations. How do I balance them step by step?")
# print(str(result))
