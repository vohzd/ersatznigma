# -*- python -*-

import random

class Format:
    def generate(self):
        raise Exception("you must provide your own generate method")

    def int2group(self, n, pad=None):
        out = [ ]
        x = '{}'.format(n)
        if isinstance(pad, int):
            y = '0' * (pad - len(x))
            x = y + x
        return [c for c in '{}'.format(x)]

class ESingleMessage(Format):
    def __init__(self, schedule_id):
        self.schedule_id = schedule_id

    def message(self):
        m = list()
        for i in range(self.groupcount):
            m.append(self.int2group(int(random.random() * 100000), pad=5))
        return m

    def generate(self):
        return self.intro() + self.preamble() + self.message() + self.outro()

    def outro(self):
            return [ self.int2group(0, pad=3) ] * 2

class ENonTraffic(Format):
    def __init__(self, schedule_id):
        self.schedule_id = schedule_id

    def generate(self):
        return ( [ self.int2group(self.schedule_id) ] * 3 + [ self.int2group(0, pad=3) ] ) * int(120 / 16)

class E06NonTraffic(ENonTraffic):
    """
    http://priyom.org/number-stations/english/e06
    """
    def __init__(self):
        super().__init__(376)

    def generate(self):
        return ( [ self.int2group(self.schedule_id) ] * 3 + [ self.int2group(0, pad=5) ] ) * int(240 / 18)

class E06SingleMessage(ESingleMessage):
    """
    http://priyom.org/number-stations/english/e06
    """
    def __init__(self, slope, intercept):
        super().__init__(460)
        self.unknown = int(random.random() * 1000)
        self.groupcount = int(random.random() * slope) + intercept

    def generate(self):
        return self.intro() + self.preamble() + self.message() + self.postamble() + self.outro()

    def intro(self):
        return [ self.int2group(self.schedule_id) ] * 60

    def preamble(self):
        return [ self.int2group(self.unknown, pad=3) ] * 2 + [ self.int2group(self.groupcount) ] * 2

    def message(self):
        m = list()
        for i in range(self.groupcount):
            j = self.int2group(int(random.random() * 100000), pad=5)
            m.append(j)
            m.append(j)
        return m

    def postamble(self):
        return self.preamble()

    def outro(self):
        return [ self.int2group(0, pad=5) ]

class E06DoubleMessage(Format):
    """
    http://priyom.org/number-stations/english/e06
    """
    def __init__(self, slope, intercept):
        super().__init__(509)
        self.unknown = [ int(random.random() * 1000), int(random.random() * 1000) ]
        self.groupcount = [ int(random.random() * slope) + intercept, int(random.random() * slope) + intercept ]

    def generate(self):
        return self.first_intro() + self.first_preamble() + self.first_message() + self.first_postamble() + self.second_intro() + self.second_preamble() + self.second_message() + self.second_postamble() + self.outro()

    def intro(self, duration):
        return [ self.int2group(self.schedule_id) ] * int(duration / 4)

    def first_intro(self):
        return self.intro(240)

    def second_intro(self):
        return self.intro(60)

    def preamble(self, n):
        return [ self.int2group(self.unknown[n]) ] * 2 + [ self.int2group(self.groupcount[n]) ] * 2

    def first_preamble(self):
        return self.preamble(0)

    def second_preamble(self):
        return self.preamble(1)

    def first_postamble(self):
        return self.first_preamble()

    def second_postamble(self):
        return self.second_preamble()

    def message(self, n):
        m = list()
        for i in range(self.groupcount[n]):
            j = self.int2group(int(random.random() * 100000), pad=5)
            m.append(j)
            m.append(j)
        return m

    def first_message(self):
        return self.message(0)

    def second_message(self):
        return self.message(1)

    def outro(self):
        return [ self.int2group(0, pad=5) ]

class E07aNonTraffic(ENonTraffic):
    """
    http://priyom.org/number-stations/english/e07a
    """
    def __init__(self):
        super().__init__(147)

class E07aSingleMessage(ESingleMessage):
    """
    http://priyom.org/number-stations/english/e07a
    """
    def __init__(self, slope, intercept):
        super().__init__(318)
        self.unknown = [ int(random.random() * 100000), int(random.random() * 9900) + 100 ]
        self.groupcount = int(random.random() * slope) + intercept

    def intro(self):
        return (
            [ self.int2group(self.schedule_id) ] * 3
            +
            [ [ '1' ] ]
            +
            [ self.int2group(self.unknown[0], pad=5) ]
        ) * 6

    def preamble(self):
        return [
            self.int2group(self.unknown[1]),
            self.int2group(self.groupcount)
        ] * 2

class E07NonTraffic(ENonTraffic):
    """
    http://priyom.org/number-stations/english/e07
    """
    def __init__(self):
        super().__init__(553)

class E07SingleMessage(ESingleMessage):
    """
    http://priyom.org/number-stations/english/e07
    """
    def __init__(self, slope, intercept):
        super().__init__(845)
        self.unknown = int(random.random() * 9900) + 100
        self.groupcount = int(random.random() * slope) + intercept

    def intro(self):
        return ( [ self.int2group(self.schedule_id) ] * 3 + [ [ '1' ] ] ) * int(120 / 14)

    def preamble(self):
        return [ self.int2group(self.unknown), self.int2group(self.groupcount) ] * 2

class E07DoubleMessage(Format):
    """
    http://priyom.org/number-stations/english/e07
    """
    def __init__(self, slope, intercept):
        self.schedule_id = 124
        self.unknown = [ int(random.random() * 9900) + 100, int(random.random() * 9900) + 100 ]
        self.groupcount = [ int(random.random() * slope) + intercept, int(random.random() * slope) + intercept ]

    def generate(self):
        return self.first_intro() + self.first_preamble() + self.first_message() + self.second_intro() + self.second_preamble() + self.second_message() + self.outro()

    def intro(self, duration):
        return ( [ self.int2group(self.schedule_id) ] * 3 + [ [ '2' ] ] ) * int(duration / 14)

    def first_intro(self):
        return self.intro(120)

    def second_intro(self):
        return self.intro(60)

    def preamble(self, n):
        return [ self.int2group(self.unknown[n]), self.int2group(self.groupcount[n]) ] * 2

    def first_preamble(self):
        return self.preamble(0)

    def second_preamble(self):
        return self.preamble(1)

    def message(self, index):
        m = list()
        for i in range(self.groupcount[index]):
            m.append(self.int2group(int(random.random() * 100000), pad=5))
        return m

    def first_message(self):
        return self.message(0)

    def second_message(self):
        return self.message(1)

    def outro(self):
        return [ self.int2group(0, pad=3) ] * 2
