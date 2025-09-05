class Event:
    def __init__(self, event:str):
        self.event = event

        self.m1_pt = None
        self.m1_eta = None
        self.m1_phi = None
        self.m1_m = None
        self.m1_px = None
        self.m1_py = None
        self.m1_pz = None
        self.m1_e = None
        self.m1_fvector = None
        self.m1_imass = None
        

        self.m2_pt = None
        self.m2_eta = None
        self.m2_phi = None
        self.m2_m = None
        self.m2_px = None
        self.m2_py = None
        self.m2_pz = None
        self.m2_e = None
        self.m2_fvector = None
        self.m2_imass = None

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


    

        

    def muons_collector(self, muon_info:str) -> list:
        begin_index = muon_info.find("=")
        end_index = muon_info.index("dptinv")
        data_list = muon_info[begin_index+1:end_index].strip(" ").split(" ")
        return data_list
