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
