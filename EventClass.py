class Event:
    def __init__(self, event:str):
        self.event = event
        self.muon_one = None
        self.muon_two = None

    def muon_one_setter(self, m1:str):
        data_collected = self.muons_collector(m1)
        self.m1_pt = data_collected[0]
        self.m1_eta = data_collected[1]
        self.m1_phi = data_collected[2]
        self.m1_m = data_collected[3]
        

    def muon_two_setter(self, m2:str):
        data_collected = self.muons_collector(m2)
        self.m2_pt = data_collected[0]
        self.m2_eta = data_collected[1]
        self.m2_phi = data_collected[2]
        self.m2_m = data_collected[3]

    def momentum_formula(self) -> int:
        """
        px = pt cos theta (phi)
        py = pt sin theta (phi)
        pz = pt sinh(eta)

        p = sqrt (px2 + py2 + pz2)
        """
