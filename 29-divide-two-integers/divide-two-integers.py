class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        con = 0

        while dividend >= divisor:
            temp = divisor
            count = 1

            while dividend >= temp + temp:
                temp = temp + temp
                count = count + count

            dividend = dividend - temp
            con = con + count

        if negative:
            con = -con

        if con > 2147483647:
            con = 2147483647

        if con < -2147483648:
            con = -2147483648

        return con