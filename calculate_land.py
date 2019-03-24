class Rect:
    def __init__(self, lindex, rindex, start = 0, end = 0):
        self.lindex = lindex
        self.rindex = rindex
        self.start = start
        self.end = end
    
    def base(self):
        return self.rindex - self.lindex + 1
    
    def height(self):
        return self.end - self.start + 1

    def bump_rindex(self):
        self.rindex += 1
    
    def bump_end(self):
        self.end += 1

    def area(self):
        return self.base() * self.height()

    def shares_base_with(self, other_rect):
        if self.lindex <= other_rect.rindex and self.lindex >= other_rect.lindex:
            return True
        if self.rindex >= other_rect.lindex and self.rindex <= other_rect.rindex:
            return True
        return False

    def combine_rects(self, other_rect):
        # assumes self is an active_rect and other_rect is a row_rect
        l = max([self.lindex, other_rect.lindex])
        r = min([self.rindex, other_rect.rindex])
        s = self.start
        e = self.end + 1
        return Rect(l, r, s, e)
    
    def contained_within(self, other_rect):
        return self.lindex >= other_rect.lindex and self.rindex <= other_rect.rindex

class Land_Plot:
    def __init__(self, matrix, fertile_symbol):
        self.matrix = matrix
        self.active_rects = []
        self.largest_rect = Rect(1,0)
        self.active_row = 0
        self.fertile_symbol = fertile_symbol

    def process_all_rows(self):
        self.__init__(self.matrix, self.fertile_symbol)
        while(self.active_row < len(self.matrix)):
            self.process_row()
        self.retire_rects(self.active_rects)
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

                
