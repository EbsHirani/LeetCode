class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence = " ".join(sentence) + " "

        pointer = 0

        for i in range(rows):
            pointer+=cols
            if sentence[pointer%len(sentence)] == " ":
                pointer+=1
            else:
                while pointer>0 and sentence[pointer%len(sentence)-1] != " ":
                    pointer-=1
        
        return pointer//len(sentence)
        
            