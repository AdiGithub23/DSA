
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        ch_index = word.find(ch)  # Find the index of the first occurrence of ch
        if ch_index < -1:  # If ch is not found, return the original string
            return word    

        word_portion_1 = word[:ch_index + 1]
        word_portion_2 = word[ch_index + 1:]

        reverse_portion = ''
        for s in word_portion_1:
            reverse_portion = s + reverse_portion
        """ 
        String Reversal can be done as follows as well...
            
            Method_1:-
            reverse_portion = word_portion_1[::-1]

            Method_2:-
            reverse_portion = ''.join(reversed(word_portion_1))
        """

        answer = reverse_portion + word_portion_2
        return answer
        
solution_1 = Solution()                                         # Creating an instance of the class
reversePrefix_answer = solution_1.reversePrefix('abcdefg', 'd') # Calling the function

print("\n", reversePrefix_answer, "\n")
