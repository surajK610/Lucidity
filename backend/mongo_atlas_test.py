from pymongo import MongoClient
import os
import certifi

def main():
    db_usr, db_pswrd = 'cs32FinalProject', 'cs32FinalProject'
    print(f'user is {db_usr}')
    print(f'password is {db_pswrd}')
    uri = 'mongodb+srv://cs32FinalProject:cs32FinalProject@cluster0.ovkaf.mongodb.net/lucidity?retryWrites=true&w=majority'
    client = MongoClient(uri, tlsCAFile=certifi.where())
    
    db = client.lucidity

    print(db)

    celebData = db.celebData

    print(celebData)

    res = celebData.find_one({'name':'Elon Musk'})
    print(res)

    client.close()



if __name__ == "__main__":
    main()