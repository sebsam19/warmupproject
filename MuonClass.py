class Muon:
    def __init__(self, muon_info : str):
        self.m_info = muon_info
        self.m_pt = None
        self.m_eta = None
        self.m_phi = None
        self.m_mass = None
        self.m_px = None
        self.m_py = None
        self.m_pz = None
        self.m_e = None
        self.m_fvector = None
        self.m_imass = None
    
    def muons_collector(self, muon_info:str) -> list:
        begin_index = muon_info.find("=")
        end_index = muon_info.index("dptinv")
        data_list = muon_info[begin_index+1:end_index].strip(" ").split(" ")
        return data_list