class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count how many times the current char repeats
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the char
            chars[write] = char
            write += 1

            # If count > 1, write the digits
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
