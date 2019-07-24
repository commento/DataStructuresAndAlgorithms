
import sys
import collections


class Node:
    def __init__(self, value):
        self.right_child = None
        self.left_child = None
        self.value = value

    def set_left_child(self, node):
        self.left_child = node

    def set_right_child(self, node):
        self.right_child = node

class Tree:
    def __init__(self, root):
        self.root = root

def huffman_encoding(data):
    all_freq = {} 
  
    for char in data: 
        if char in all_freq: 
            all_freq[char] += 1
        else: 
            all_freq[char] = 1


    dict_of_tuple = {}

    for key,value in all_freq.items():
        #None will be used to store Node
        dict_of_tuple[(key, value)] = None

    sorted_dict_of_tuple = collections.OrderedDict(sorted(dict_of_tuple.items(), key=lambda kv: kv[0][1]))

    root_node = create_tree_recursive(sorted_dict_of_tuple)[1]
    
    tree = Tree(root_node)

    encoded_data = ''
    tmp = ''

    for char in data:
        tmp = encode_data_recursive(tree.root, '', char)
        if tmp is not None:
            encoded_data += tmp

    return encoded_data , tree

#encoded using https://www.siggraph.org/education/materials/HyperGraph/video/mpeg/mpegfaq/huffman_tutorial.html
def encode_data_recursive(node, path, char):
    returned_path = ''

    if node.left_child is None and node.right_child is None and node.value[0] == char:
        return path
    if node.left_child is not None:
        path_left = path + '0'
        #traverse left hand
        returned_path_left = encode_data_recursive(node.left_child, path_left, char)
        if returned_path_left is not None:
            return returned_path_left
    if node.right_child is not None:
        path_right = path + '1'
        #traverse right hand
        returned_path_right = encode_data_recursive(node.right_child, path_right, char)
        if returned_path_right is not None:
            return returned_path_right

def create_tree_recursive(sorted_dict_of_tuple):

    if len(sorted_dict_of_tuple) == 1:
        return sorted_dict_of_tuple.popitem()

    #pop from the first two elem of soted_dict (less frequent)
    kv0 = sorted_dict_of_tuple.popitem(last=False)
    kv1 = sorted_dict_of_tuple.popitem(last=False)

    #add them to newly created nodes if not present already
    if kv0[1] is None:
        n0 = Node(kv0[0])
    else:
        n0 = kv0[1]

    if kv1[1] is None:
        n1 = Node(kv1[0])
    else:
        n1 = kv1[1]

    #create a parent node that has them as childs
    p_value = (kv0[0][0]+kv1[0][0], kv0[0][1]+kv1[0][1])
    p_n = Node(p_value)
    p_n.set_left_child(n0)
    p_n.set_right_child(n1)

    #update the sorted_dict_of_tuple
    sorted_dict_of_tuple.update({(p_value[0],p_value[1]) : p_n})

    #reorder sorted_dict_of_tuple
    sorted_dict_of_tuple = collections.OrderedDict(sorted(sorted_dict_of_tuple.items(), key=lambda kv: kv[0][1]))

    return create_tree_recursive(sorted_dict_of_tuple)

def huffman_decoding(data,tree):

    decoded_data = ''
    data_left = data

    while data_left != '':
        decoded_letter, data_left = decode_recursive(data_left,tree.root)
        decoded_data += decoded_letter

    return decoded_data
    
def decode_recursive(data, node):

    if node.left_child is None and node.right_child is None:
        return node.value[0], data
    elif data[0] == '0' and node.left_child is not None:
        char, data = decode_recursive(data[1:], node.left_child)
        if char is not None:
            return char , data
    elif data[0] == '1' and node.right_child is not None:
        char, data = decode_recursive(data[1:], node.right_child)
        if char is not None:
            return char , data

if __name__ == "__main__":
    codes = {}

    print("Test 1: Normal scenario")

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    print("Test 2: Short sequence")

    a_great_sentence = "az"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    print("Test 3: Long sequence")

    a_great_sentence = "Es gibt im Moment in diese Mannschaft, oh, einige Spieler vergessen ihnen Profi was sie sind. Ich lese nicht sehr viele Zeitungen, aber ich habe gehört viele Situationen. Erstens: wir haben nicht offensiv gespielt. Es gibt keine deutsche Mannschaft spielt offensiv und die Name offensiv wie Bayern. Letzte Spiel hatten wir in Platz drei Spitzen: Elber, Jancka und dann Zickler. Wir müssen nicht vergessen Zickler. Zickler ist eine Spitzen mehr, Mehmet eh mehr Basler. Ist klar diese Wörter, ist möglich verstehen, was ich hab gesagt? Danke. Offensiv, offensiv ist wie machen wir in Platz. Zweitens: ich habe erklärt mit diese zwei Spieler: nach Dortmund brauchen vielleicht Halbzeit Pause. Ich habe auch andere Mannschaften gesehen in Europa nach diese Mittwoch. Ich habe gesehen auch zwei Tage die Training. Ein Trainer ist nicht ein Idiot! Ein Trainer sei sehen was passieren in Platz. In diese Spiel es waren zwei, drei diese Spieler waren schwach wie eine Flasche leer! Haben Sie gesehen Mittwoch, welche Mannschaft hat gespielt Mittwoch? Hat gespielt Mehmet oder gespielt Basler oder hat gespielt Trapattoni? Diese Spieler beklagen mehr als sie spielen! Wissen Sie, warum die Italienmannschaften kaufen nicht diese Spieler? Weil wir haben gesehen viele Male solche Spiel! Haben"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
