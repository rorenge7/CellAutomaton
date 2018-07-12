import cell
import random

class Automaton(list):
    def __str__(self):
        return ' '.join(list(map(lambda cell: str(cell), self)))

    def step(self):
        for cell in self:
            cell.calc()
        for cell in self:
            cell.update()

    def setup(self, ring_size,car_num):
        val_list = []

        for index in range(ring_size ):
            val_list.append(1 if index < car_num else 0)
        random.shuffle(val_list)

        for index in range(ring_size):
            set_val = val_list[index]
            self.append(cell.cell_184(set_val))

        for index in range(ring_size):
            self[index].prev = self[(index - 1) % ring_size]
            self[index].next = self[(index + 1) % ring_size]



class AutomatonAlt(Automaton):
    def __str__(self):
        main = ' '.join(list(map(lambda cell: str(cell), self)))
        alt = ' '.join(list(map(lambda cell: str(cell), self.alt)))
        return main + '\n'+(" "*(2*(self.start+1))) + alt

    def strMain(self):
        return ' '.join(list(map(lambda cell: str(cell), self)))

    def strAlt(self):
        return ' '.join(list(map(lambda cell: str(cell), self.alt)))

    def set_alt(self, alt, start, end):
        self.alt = alt
        self.start = start
        self.end = end

    def step(self):
        for cell in self:
            cell.calc()
        for cell in self.alt:
            cell.calc()
        for cell in self:
            cell.update()
        for cell in self.alt:
            cell.update()

    def setup(self,branch_index, connecting_index,ring_size, alt_size,car_num):
        self.alt = []
        self.start = branch_index
        self.end = connecting_index

        val_list = []
        for index in range(ring_size + alt_size):
            val_list.append(1 if index<car_num else 0)

        random.shuffle(val_list)
        main_list = val_list[0:ring_size]
        alt_list = val_list[ring_size:ring_size+alt_size]

        for index in range(ring_size):
            set_val = main_list[index]
            if index == branch_index:
                self.append(cell.branch(set_val))
            elif index == connecting_index:
                self.append(cell.connecting(set_val))
            else:
                self.append(cell.cell_184(set_val))

        for index in range(ring_size):
            self[index].prev = self[(index - 1) % ring_size]
            self[index].next = self[(index + 1) % ring_size]

        for index in range(alt_size):
            set_val= alt_list[index]
            if index == 0:
                self.alt.append(cell.side_start(set_val))
            elif index == alt_size - 1:
                self.alt.append(cell.side_end(set_val))
            else:
                self.alt.append(cell.cell_184(set_val))

        for index in range(alt_size):
            self.alt[index].prev = self.alt[(index - 1) % alt_size]
            self.alt[index].next = self.alt[(index + 1) % alt_size]

        self[branch_index].alt = self.alt[0]
        self.alt[0].prev = self[branch_index]
        self.alt[0].alt = self[(branch_index + 1) % ring_size]
        self[connecting_index].alt = self.alt[alt_size-1]
        self.alt[alt_size-1].next = self[connecting_index]
        self.alt[alt_size -
                    1].alt = self[(connecting_index - 1) % ring_size]
