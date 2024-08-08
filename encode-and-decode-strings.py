class Codec:
	def encode(self, strs) -> str:
		encoder = "--msg-->"
		fin_str = ''
		fin_str = encoder.join(strs)
		return fin_str
	
	def decode(self, s):
		return s.split('--msg-->')

#inputs
dummy_input_one = ["Hello", "World"]

codec = Codec()

print(dummy_input_one)
encoded_msg = codec.encode(dummy_input_one)
print(codec.decode(encoded_msg))

