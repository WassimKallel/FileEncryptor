# FileEncryptor
A memory versatile file encryptor using the famous XOR function, written in Python 3 and runs efficiently with low memory usage.

## Usage

First clone the project and go into its directory by executing the commands

```shell
git clone https://github.com/WassimKallel/FileEncryptor
cd FileEncryptor
```

### Encrypt a file
Now, make sure you have python 3 installed and you'll able to run the script and encrypt a file

```shell
python3 xor.py super_secret_file.txt my_secret_key encrypted_file_output.txt
```
You should always remember your secret key to decrypt the file


### Decrypt a file
Since XOR is a symmetric decrypting an encrypted file uses the same script and requires only the secret of the encryption

```shell
python3 xor.py encrypted_file.txt the_same_secret decrypted_file.txt
```

### Go beyond files with directories
You're also able to encrypt a directory with all its content just by providing a directory path as an argument

```shell
python3 xor.py original_directory_path/ my_secret_key encrypted_directory_path/
```

### The Unix Pipeline is awesome
If you don't specify an output file, then the encrypted data will be redirected to standard output of your terminal, so you're able to pipe it to another command that comes after
```shell
python3 xor.py super_secret_file.txt my_secret_key | cat > encrypted_file
```