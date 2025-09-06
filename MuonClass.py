import math

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
        self.m_mntm = None
    
    def muons_collector(self) -> list:
        begin_index = self.m_info.find("=")
        end_index = self.m_info.index("dptinv")
        data_list = self.m_info[begin_index+1:end_index].strip(" ").split(" ")
        return data_list
    
    def muons_setters(self) -> None:
        data_list = self.muons_collector()
        self.m_pt = data_list[0]
        self.m_eta = data_list[1]
        self.m_phi = data_list[2]
        self.m_mass = data_list[3]
    
    def momentum_calc(self) -> None:
        self.m_px = self.m_pt * math.cos(self.m_phi)
        self.m_py = self.m_pt * math.sin(self.m_phi)
        self.m_pz = self.m_pt * math.sinh(self.m_eta)

        self.m_mntm = math.sqrt((self.m_px ** 2) + (self.m_py ** 2) + (self.m_pz ** 2))
    
    def energy_calc(self) -> None:
        """
        e = sqrt ( mass ^ 2 + mom ^ 2)
        """
        self.m_e = math.sqrt((self.m_mass ** 2) + (self.m_mntm ** 2))
    
    def 