class Return_Words():
    def __init__(self):
        # self.ctx_source = ctx
        self.word_lists = []
    
    def get_words(self):
        return self.word_lists
    
    def return_children_number(self, parent):
        try:
            num = len(parent.children)
        except AttributeError:  # 子を持っていないとき
            num = 0
        return num
    
    def make_list(self, ctx):
        num = self.return_children_number(ctx)
        if num != 0:
            for i in range(num):
                child = ctx.getChild(i)
                self.make_list(child)
        else:
            # self.word_lists.append((ctx.getText(), type(ctx)))
            self.word_lists.append(ctx.getText())
        
    