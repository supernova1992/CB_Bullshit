from textgenrnn import textgenrnn

textgen = textgenrnn(weights_path='cbchat_full_weights.hdf5',
						vocab_path='cbchat_full_vocab.json',
						config_path='cbchat_full_config.json')

print(textgen.generate(1, return_as_list=True)[0])