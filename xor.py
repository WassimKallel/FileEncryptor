import sys
from os import path, walk, sep, makedirs

def get_next_byte_from_needle(bytes_array):
    i = 0
    while True:
        yield bytes_array[i]
        i = (i + 1) % len(bytes_array)

def encrypt_file(secret_string, input_path, output_path=None):

    encoded_secret = secret_string.encode('ascii')
    secret_bytes_gen = get_next_byte_from_needle(encoded_secret)

    try: 
        with open(input_path, 'rb') as file_to_encode, open(output_path, 'wb') if output_path else sys.stdout.buffer as output_file:
            to_encode_content_byte = file_to_encode.read(1)
            while(to_encode_content_byte != b''):
                to_encode_int_value = int.from_bytes(to_encode_content_byte,byteorder=sys.byteorder)
                output_file.write(bytes([to_encode_int_value ^ next(secret_bytes_gen)]))
                to_encode_content_byte = file_to_encode.read(1)
    except IOError as e:
        print(e)

def encrypt_directory(secret_string, input_path, output_path):
    for dir_name, _, files_list in walk(input_path):
        for file in files_list:
            secret_file_path = path.join(dir_name, file)
            output_file_path = path.join(output_path, *(secret_file_path.split(sep)[1:]))
            if not path.isdir(path.split(output_file_path)[0]):
                makedirs(path.split(output_file_path)[0])
            encrypt_file(secret_string, secret_file_path, output_file_path)

def main():
    if len(sys.argv) < 3:
        print(
        '''
            Insuffisant arguments provided
            try executing the script using three parameters
                1 - secret file/folder
                2 - secret string
                3 - output(encrypted) file/folder (Optional)
            Example: python3 xor.py super_secret_file.txt my_secret_key encrypted_file.txt
        ''')
        sys.exit(1)
    
    input_path = sys.argv[1]
    secret_string = sys.argv[2]
    output_path = None
    if len(sys.argv) > 3:
        output_path = sys.argv[3]

    if path.isfile(input_path):
        is_reccursive = False
    elif path.isdir(input_path):
        if output_path != None:
            is_reccursive = True
        else:
            print('You should specify an output directory')
            sys.exit(1)
    else:
        print('invalid input path provided')
        sys.exit(1)

    if output_path:
        if path.isfile(output_path) or path.isdir(output_path):
            print('output path already exists')
            sys.exit(1)

    if not is_reccursive:
        encrypt_file(secret_string, input_path, output_path)
    else:
        encrypt_directory(secret_string, input_path, output_path)

if __name__ == '__main__':
    main()