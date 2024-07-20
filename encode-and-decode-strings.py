class Codec:
    #they obviously want to see that you know how to mutate strings properly here
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoder = '--msg-->'
        fin_word = ''
        
        fin_word = encoder.join(strs)
        print(fin_word)
        return fin_word

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('--msg-->')
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
