from PIL import Image

def encode_message(image, message):
    encode_image = image.copy()
    width, height = image.size
    message += "####"
    message_bits = ''.join([format(ord(char), '08b') for char in message])
    data_index = 0

    for y in range(height):
        for x in range(width):
            if data_index < len(message_bits):
                pixel = list(image.getpixel((x,y)))
                for n in range(3):
                    if data_index < len(message_bits):
                        pixel[n] = pixel[n] & ~1 | int(message_bits[data_index])
                        data_index +=1 
                encode_image.putpixel((x,y), tuple(pixel))
            else:
                break
    return encode_image


def decode_message(image):
    width, height = image.size
    message_bits = []
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x,y))
            for b in range(3):
                message_bits.append(pixel[b] & 1)
        message_bytes = [message_bits[i:i+8] for i in range(0, len(message_bits), 8)]
        message = ''.join([chr(int(''.join(map(str, byte)), 2)) for byte in message_bytes])
        return message.split('####')[0]


if __name__ == '__main__':
    # Load the image
    input_image_path = 'test.png'
    output_image_path = 'encoded_image.png'
    image = Image.open(input_image_path)
    image.show()

    # Encode a message
    secret_message = "Hello, this is Codestam!"
    encoded_image = encode_message(image, secret_message)
    encoded_image.save(output_image_path)

    # Decode the message
    decoded_image = Image.open(output_image_path)
    decoded_message = decode_message(decoded_image)
    print("Decoded Message:", decoded_message)
