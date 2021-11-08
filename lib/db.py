import pymongo
from . import config
from . import logger

def connect(dbargs):
    logger.writeLog('connect()...')
    myclient = pymongo.MongoClient(dbargs['address'])
    mydb = myclient[dbargs['database']]
    mycol = mydb[dbargs['collection']]
    return mycol

def insertOne(collection):
    logger.writeLog('insertOne()...')
    mycol = connect(config.albums)
    found = False
    if mycol.find({'name':collection['name']}).count() > 0:
        found = True
    if not found:
        mycol.insert_one(collection)

def aggregate():
    logger.writeLog('aggregate()...')
    mycol = connect(config.albums)
    for document in mycol.find({
            'producers' : {'$in' : ['sez on the beat']},
            'artist' : {'$in' : ['seedhe maut']},
            'tags' : {'$in' : ['trap']}
    }):
        logger.writeLog(document)

def insertArtist(artistData):
    logger.writeLog('insertArtist()...')
    mycol = connect(config.artists)
    mycol.insert({
        'name' : artistData['name'],
        'spotify_id' : artistData['spotify_id'],
        'total' : 0
    })

def updateArtist(artistData,updatedData):
    logger.writeLog('updateArtist()...')
    mycol = connect(config.artists)
    mycol.update_one({'name' : artistData['name']},
                     {'$set': updatedData})

def fetchMetaData(artist):
    logger.writeLog('fetchMetaData()...')
    mycol = connect(config.artists)
    return mycol.find_one({
            'artist' : artist
    })
