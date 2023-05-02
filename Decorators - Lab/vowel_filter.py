def vowel_filter(function):

    def wrapper():

        unfiltered = function()
        return [char for char in unfiltered if char in "ayoueiAYOUEI"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
