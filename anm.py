import zlib
import io

file = 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Brawlhalla\\anims\\Animation_Pistols.anm'
string_array = []

def start_bytes(file_path):

	dataBuffer = open(file_path, 'rb')
	first_bytes = dataBuffer.read(4)
	
	return first_bytes

def anm_data(file_path):
	
	dataBuffer = open(file_path, 'rb')
	dataBuffer.seek(4,0)
	resultdata = zlib.decompress(dataBuffer.read())

	return resultdata

def recompress(data):
	
	return zlib.compress(data, 9)
    
def save_file():
	
	out_file = open(get_file_name(file), "wb") # open for [w]riting as [b]inary
	out_file.write(start_bytes)
	out_file.write(anm_data(file))
	out_file.close()

def save_hex():
	
	out_file = open(get_file_name(file).split('.')[0] + ".hex", "wb") # open for [w]riting as [b]inary
	out_file.write(anm_data(file))
	out_file.close()

def get_file_name(file_path):

	return file_path.split('\\')[-1]

def charify(data):
	char_list = []

	for i in data:
		char_list.append(chr(i))

	return char_list


def first_byte(byte_stream):
	
	return byte_stream.read(1)


def byte_to_int(byte):
	endianess = "little"
	return int.from_bytes(byte, byteorder=endianess)


def readUTF(bytes_stream):
	UTF_String_Lenght = byte_to_int(bytes_stream.read(1))
	bytes_stream.seek(1,1)
	return bytes_stream.read(UTF_String_Lenght)

def readUnsignedInt(bytes_stream):
	return byte_to_int(bytes_stream.read(4))


raw_data = anm_data(file)
readable_data = io.BytesIO(raw_data)


while byte_to_int(first_byte(readable_data)):

	print(readUTF(readable_data))

	print(f"ActionScript file prefix: {readUTF(readable_data)}")
	print(readUTF(readable_data))
	print()

	anm_chunk_size = readUnsignedInt(readable_data)

	for i in range(anm_chunk_size):

		print(readUTF(readable_data))
		print(readUnsignedInt(readable_data))
		print(readUnsignedInt(readable_data))
		print(readUnsignedInt(readable_data))
		print(readUnsignedInt(readable_data))
		print(readUnsignedInt(readable_data))
		print(readUnsignedInt(readable_data))
		print(readUnsignedInt(readable_data))

		footer_int = readUnsignedInt(readable_data)
		pos = readable_data.tell()

		
		readable_data.seek(footer_int + pos, 0)
		
		print()

		
	#print("------------------------")
	#print( + footer_int)
	#print("------------------------")


#print(byte_to_int(first_byte(readable_data)))




#pointer = 0
#
#for i in range(len(data)):
#
#	
#
#	if data[0] == 1:
#
#		print(chr(data[i]))


		




