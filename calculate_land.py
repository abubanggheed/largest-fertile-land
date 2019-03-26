from rect import Rect

class Land_Plot:
    def __init__(self, matrix, fertile_symbol):
        self.matrix = matrix
        self.active_rects = []
        self.largest_rect = Rect(1,0)
        self.active_row = 0
        self.fertile_symbol = fertile_symbol
        self.all_rects = [self.largest_rect]

    def process_all_rows(self):
        self.__init__(self.matrix, self.fertile_symbol)
        while(self.active_row < len(self.matrix)):
            self.process_row()
        self.retire_rects(self.active_rects)
        self.sort_all_rects()
        return self.largest_rect

    def process_row(self):
        row = self.matrix[self.active_row]
        row_rects = self.make_rects(row)
        self.append_row(row_rects)
        self.active_row += 1

    def make_rects(self, row):
        i = 0
        rects = []
        current_rect = None
        while i < len(row):
            if row[i] == self.fertile_symbol:
                if current_rect == None:
                    current_rect = Rect(i, i)
                    rects.append(current_rect)
                else:
                    current_rect.bump_rindex()
            else:
                current_rect = None
            i += 1
        return rects

    def append_row(self, row_rects):
        '''
        1: active_rects that are not contained within one of the row_rects are
        retired. active_rects that are have their height increased by 1.

        2: row_rects that are not contained within an active_rect start a new
        active_rect with a height of 1

        3: when an active_rect and row_rect share part of a base, but the active_rect is
        not contained within the row_rect, a new active_rect is created with a
        height of the active_rect + 1, and a base of the shared base.
        '''
        to_retire = []
        to_append = []
        i = 0
        while i < len(row_rects):
            j = 0
            rr = row_rects[i]
            append_later = True
            while j < len(self.active_rects):
                ar = self.active_rects[j]
                if rr.shares_base_with(ar):
                    # ar and rr interact
                    if ar.contained_within(rr):
                        if rr.contained_within(ar):
                            # 1
                            ar.bump_end()
                            append_later = False
                        else:
                            # 1 and 2
                            ar.bump_end()
                    elif rr.contained_within(ar):
                        # 1 and 3
                        to_retire.append(ar)
                        to_append.append(ar.combine_rects(rr))
                        append_later = False
                    else:
                        to_retire.append(ar)
                        to_append.append(ar.combine_rects(rr))
                        # 1 2 and 3
                j += 1
            if append_later:
                to_append.append(Rect(rr.lindex, rr.rindex, self.active_row, self.active_row))
            i += 1
        # end while loops
        self.retire_rects(to_retire)
        self.active_rects += to_append
        self.all_rects += to_append

    def retire_rects(self, rects_to_retire):
        new_active_rects = []
        for i in range(0, len(self.active_rects)):
            current_rect = self.active_rects[i]
            if current_rect in rects_to_retire:
                if current_rect.area() > self.largest_rect.area():
                    self.largest_rect = current_rect
            else:
                new_active_rects.append(current_rect)
        self.active_rects = new_active_rects

    def sort_all_rects(self):
        self.sort_from(0, len(self.all_rects) - 1)

    def sort_from(self, l, r):
        if r - l > 0:
            m = (l + r) // 2
            rs = self.all_rects
            if rs[l].area() > rs[m].area():
                if rs[m].area() > rs[r].area():
                    c = m
                else:
                    c = r
            elif rs[l].area() > rs[r].area():
                c = l
            else:
                c = r
            [rs[c], rs[l]] = [rs[l], rs[c]]
            i = l + 1
            j = i
            while i < r:
                if rs[i].area() > rs[l].area():
                    [rs[i], rs[j]] = [rs[j], rs[i]]
                    j += 1
                i += 1
            [rs[l], rs[j - 1]] = [rs[j - 1], rs[l]]
            self.sort_from(l, j - 1)
            self.sort_from(j, r)

                
