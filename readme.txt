this project will generate a well structured fake dataset for Shopium Project based on the following hierarchy :


User

Fabricant:
        |_____> Product[]

Fidelite:
        |_____> User

Product :
        |_____> Caetgory
        |_____> Offer[]
        |_____> Fabricant

Review  :
        |_____> Offer
        |_____> User

Category:
        |_____> Product[]

Offer   :
        |_____> Product

Ribs    :
        |_____> User


Database expected structure :

User :        _id:           ID
              nom:           string
              prenom:        string
              pays:          string
              ville:         string
              email:         string
              password:      string
              role:          string("admin", "subscriber")
              photo:         string
              cloudinary_id: ID
              verified:      Boolean(75%True/25%False)
              codeParrainage:Int (five digits)
              amis:          IDs
              friendRequest: IDs
              sendRequest:   IDs
              createdAt:     string (Date/Time)
              updatedAt:     string (Date/Time)
              date:          string (Date)
              genre:         string("H", "F")


Product :     id :           ID
              name:          string
              price:         int
              photo:         [string] (Photos Urls)
              categoryId:    category IDs
              fabricant:     fabricant ID
              offer:         offers IDs
              logo:          string (URL)
              isLiked:       Boolean(True/False)
              isnew:         Boolean(True/False)
              createdAt:     string (Date/Time)
              updateddAt:    string (Date/Time)
              barcode:       string (EAN13)

Category  :   _id:           ID
              name:          string
              createdAt:     string (Date/Time)
              updatedAt:     string (Date/Time)


Fabricant :   _id:           ID
              name:          string
              password:      string
              logo:          string
              phone:         string
              createdAt:     string (Date/Time)
              updateddAt:    string (Date/Time)

Fidelite  :   _id:           ID
              userId:        ID
              data:          string (Barcode EAN13),
              format:        string

Ribs      :   _id:           ID
              userId:        ID
              numero:        string
              type:          string
              banque:        string
              createdAt:     string (Date/Time)
              updateddAt:    string (Date/Time)