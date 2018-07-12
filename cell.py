

class cell:
    def __init__(self, val):
        self.val = val
        self.next_val = 0
        self.prev = None
        self.next = None
        self.alt = None

    def __str__(self):
        if (self.val == 0):
            return '□'
        else:
            return '■'

    def update(self):
        self.val = self.next_val




class cell_184(cell):
    # 000:*00
    # 001:*0*
    # 010:*01
    # 011:*1*
    # 100:010
    # 101:01*
    # 110:101
    # 111:11*

    # 10* ->1
    # *11 ->1

    def calc(self):
        if (self.prev.val == 1 and self.val == 0):
            self.next_val = 1
        elif (self.val == 1 and self.next.val == 1):
            self.next_val = 1
        else:
            self.next_val = 0


class branch(cell):
    # 0000:*000
    # 0001:*00*
    # 0010:*0*0
    # 0011:*0**
    # 0100:*010
    # 0101:*01*
    # 0110:*0*1
    # 0111:*1**
    # 1000:*100
    # 1001:*10*
    # 1010:*1*0
    # 1011:*1**
    # 1100:1010
    # 1101:101*
    # 1110:10*1
    # 1111:11**

    # *111->1
    # 10**->1
    def calc(self):
        if (self.val == 1 and self.next.val == 1 and self.alt.val == 1):
            self.next_val = 1
        elif (self.prev.val == 1 and self.val == 0):
            self.next_val = 1
        else:
            self.next_val = 0


class side_start(cell):

    def calc(self):
        # 0000:0
        # 0001:0
        # 0010:0
        # 0011:0
        # 0100:0
        # 0101:0
        # 0110:1
        # 0111:1
        # 1000:0
        # 1001:1
        # 1010:0
        # 1011:1
        # 1100:0
        # 1101:0
        # 1110:1
        # 1111:1

        # *11*->1
        # 10*1->1
        if (self.val == 1 and self.next.val == 1):
            self.next_val = 1
        elif (self.prev.val == 1 and self.val == 0 and self.alt.val == 1):
            self.next_val = 1
        else:
            self.next_val = 0


class connecting(cell):
    # 0000:*000
    # 0001:*100
    # 0010:*0**
    # 0011:*1**
    # 0100:*01*
    # 0101:*011
    # 0110:*1**
    # 0111:*1*1
    # 1000:*10*
    # 1001:*101
    # 1010:*1**
    # 1011:*1*1
    # 1100:101*
    # 1101:1011
    # 1110:11**
    # 1111:11*1

    # *10*->0
    # 00*0->0

    def calc(self):
        if (self.val == 1 and self.next.val == 0):
            self.next_val = 0
        elif (self.prev.val == 0 and self.val == 0 and self.alt.val == 0):
            self.next_val = 0
        else:
            self.next_val = 1


class side_end(cell):
        # 0000:0
        # 0001:0
        # 0010:0
        # 0011:0
        # 0100:0
        # 0101:1
        # 0110:1
        # 0111:1
        # 1000:1
        # 1001:1
        # 1010:1
        # 1011:1
        # 1100:0
        # 1101:1
        # 1110:1
        # 1111:1

        # *100:0
        # 00**:0

    def calc(self):
        if (self.val == 1 and self.next.val == 0 and self.alt.val == 0):
            self.next_val = 0
        elif (self.prev.val == 0 and self.val == 0):
            self.next_val = 0
        else:
            self.next_val = 1
