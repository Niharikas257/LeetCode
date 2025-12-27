class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read < len(chars):
            ch = chars[read]
            run_start = read

            while read < len(chars) and chars[read] == ch:
                read += 1
            run_length = read - run_start

            chars[write] = ch
            write += 1
            if run_length >1:
                for digits in str(run_length):
                    chars[write] = digits
                    write += 1
        return write

        