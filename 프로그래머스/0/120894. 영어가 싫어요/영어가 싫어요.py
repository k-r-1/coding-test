def solution(numbers):
    
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i, words in enumerate(words):
        numbers = numbers.replace(words, str(i))
    
    return int(numbers)