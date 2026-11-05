class Solution:
    def encode(self, strs):
        output = ''
        for i in strs:
            output += f'{len(i)}#{i}'
        return output

    def decode(self, s):
        output = []
        length = ''
        i = 0
        if s == '':
            return output
        while True:
            if list(s)[i] == '#':
                output.append(s[i+1:i+1+int(length)])
                i = i+1+int(length)
                length = ''
            if i >= len(s):
                return output
            length += list(s)[i]
            i += 1