class Building:
    def _init_(self, name, address, rent, dues):
        self.name = name
        self.address = address
        self.rent = rent
        self.dues = dues

class Tenant:
    def _init_(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

building1 = Building("Örnek Bina 1", "Örnek Adres 1", 2000, 500)
building2 = Building("Örnek Bina 2", "Örnek Adres 2", 3000, 700)
building3 = Building("Örnek Bina 3", "Örnek Adres 3", 2500, 600)

tenant1 = Tenant("Ahmet", "Yılmaz")
tenant2 = Tenant("Ayşe", "Kara")
tenant3 = Tenant("Mehmet", "Demir")

building1_tenants = [tenant1, tenant2]
building2_tenants = [tenant3]
building3_tenants = []

buildings = [building1, building2, building3]

def get_building_info(building):
    print("Bina Adı:", building.name)
    print("Adres:", building.address)
    print("Kira Bedeli:", building.rent)
    print("Aidat Bedeli:", building.dues)

def get_tenant_info(tenant):
    print("İsim:", tenant.first_name)
    print("Soyisim:", tenant.last_name)

def show_all_buildings():
    for building in buildings:
        get_building_info(building)
        print("Kiracılar:")
        if building == building1:
            for tenant in building1_tenants:
                get_tenant_info(tenant)
        elif building == building2:
            for tenant in building2_tenants:
                get_tenant_info(tenant)
        elif building == building3:
            for tenant in building3_tenants:
                get_tenant_info(tenant)
        print("------------")

show_all_buildings()