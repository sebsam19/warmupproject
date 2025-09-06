import math

class Muon:
    """muon class holds all the data necessary to each individual muon
    holds the pt, eta, phi, mass, the momentum and its 4 coordinates, energy, four-vector
    """
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
        self.m_mntm = None
    
    def muons_collector(self) -> list:
        """extracts the floats from the file that was read for each event"""
        begin_index = self.m_info.find("=")
        end_index = self.m_info.index("dptinv")
        data_list = self.m_info[begin_index+1:end_index].strip(" ").split(" ")
        return data_list
    
    def muons_setters(self) -> None:
        """sets up pt, eta, phi, mass for the specific Muon object"""
        data_list = self.muons_collector()
        self.m_pt = float(data_list[0])
        self.m_eta = float(data_list[1])
        self.m_phi = float(data_list[2])
        self.m_mass = float(data_list[3])
    
    def momentum_calc(self) -> None:
        """calculates the momentum"""
        self.m_px = self.m_pt * math.cos(self.m_phi)
        self.m_py = self.m_pt * math.sin(self.m_phi)
        self.m_pz = self.m_pt * math.sinh(self.m_eta)

        self.m_mntm = math.sqrt((self.m_px ** 2) + (self.m_py ** 2) + (self.m_pz ** 2))
    
    def energy_calc(self) -> None:
        """calculates the energy"""
        self.m_e = math.sqrt((self.m_mass ** 2) + (self.m_mntm ** 2))
    
    def vector_calc(self) -> None:
        """calculates the 4-vector"""
        # self.m_fvector = self.m_mntm + self.m_e
        self.m_fvector = (self.m_e, self.m_px, self.m_py, self.m_pz)
    
    def energy_getter(self) -> float:
        """returns energy"""
        return self.m_e
    
    def mass_getter(self) -> float:
        """returns mass"""
        return self.m_mass
    
    def momentum_getter(self) -> set:
        """returns momentum"""
        return self.m_mntm