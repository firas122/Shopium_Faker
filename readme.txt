this project will generate a well structured fake dataset for Shopium Project based on the following hierarchy :

User

Fabricant:
        |-----> Product[]

Fidelite:
        |-----> User

Product:
        |-----> Caetgory
        |-----> Offer[]
        |-----> Fabricant

Review:
        |-----> Offer
        |-----> User

Category:
        |-----> Product[]

Offer:
        |-----> Product


to be UPDATED