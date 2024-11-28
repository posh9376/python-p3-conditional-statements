dog = 'lazy'

if dog == 'jumpy':
    print('The dog is jumpy')
elif dog == 'lazy':
    print('The dog is lazy')
else:
    print('The dog is neither jumpy nor lazy')

def my_function(value):
    if value:
        print('yep!')
    else:
        print('nope!')

age = 109

is_adult = 'adult' if age >= 18 else 'not adult'



iq = 100

is_smart = 'smart' if iq >= 80 else 'not smart'

def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")


dog = "cuddly"

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")
print(owner)