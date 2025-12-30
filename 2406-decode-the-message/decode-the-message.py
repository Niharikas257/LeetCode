class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # 1. There can not be a specific way to encode all the messages because we are considering the start of all the messages as "a".
        # 2. so we can not generalize it but we can store the values in the hashmap and while decoding we'll refer to the hash table.
        mapping = {}
        next_plain_code = ord('a')
        for k in key:
            if k == ' ':
                continue
            if k in mapping:
                continue
            mapping[k] = chr(next_plain_code)
            next_plain_code += 1
            if next_plain_code > ord('z'):
                break
        
        result = []
        for k in message:
            if k == ' ':
                result.append(' ')
            else:
                result.append(mapping[k])
        return "".join(result)


        