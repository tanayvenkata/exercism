def encode(numbers):
    result = []
    
    for number in numbers:
        if number == 0:
            result.append(0)
            continue
            
        bytes_list = []
        
        while number > 0:
            byte = number & 0x7F
            number >>= 7
            
            if bytes_list:
                byte |= 0x80
                
            bytes_list.append(byte)
        
        result.extend(reversed(bytes_list))
    
    return result


def decode(bytes_list):
    result = []
    current = 0
    incomplete = False
    
    for byte in bytes_list:
        if byte & 0x80:  # Continuation bit is set
            current = (current << 7) | (byte & 0x7F)
            incomplete = True
        else:
            current = (current << 7) | byte
            result.append(current)
            current = 0
            incomplete = False
    
    if incomplete:
        raise ValueError("incomplete sequence")
    
    return result