class Block:
    def __init__(self, mScopeId, mDecls, mStats):
        self.mScopeId = mScopeId
        # Idを入力
        self.mDecls = mDecls
        self.mStats = mStats

class Blocks:
    def __init__(self):
        self.mBlocks = []
    
    def set_block(self):
        pass
    
    def get_block(self):
        return self.mBlocks