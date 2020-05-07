class ContactList(list):
    def __init__(self,names):
        self.names = names

    def search_by_name(self,search):
        for name in self.names:
            if name == search:
                print(name)
all_contacts=ContactList(["Ivan","Masha", "Jenya","Katya","Katya"])
all_contacts.search_by_name("Masha")

