'''
parse tfrecord from Sequence example into context tensor and sequence tensor

ex: tf.Sequence_Example
cf: a dictionary with key to value mapping for context tensor
sf: a dictionary with key to value mapping for sequence tensor

return:
context_dict: dictionary for context tensors {context_key_name: context tensor}
seq_dict: dictionary for sequence tensors {seq_key_name: seq tensor}
'''
def parse_seq_example(ex, cf, sf):
    context_dict = {}
    seq_dict = {}
    context, sequence = tf.parse_single_sequence_example(ex, context_features=cf, sequence_features=sf)
    for key in cf.keys():
        context_dict[key] = context[key]
    for key in sf.keys()；
        seq_dict[key] = sequence[key]
    return context_dict, seq_dict