import pymongo
from utils import get_user_profile,get_problem_data
import logging

logging.basicConfig(filename="leetraker.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)

client = pymongo.MongoClient("mongodb://madhav:madhav@192.168.1.123:1405/?authMechanism=DEFAULT")


# Create a new database named "telegramdb"
telegramdb = client["telegramdb"]

# Create a new collection named "users" and questions
users = telegramdb["users"]
questions = users["questions"]

def insert_user(userid, username):
    existing_doc = users.find_one({"userid": userid})
    if existing_doc:
        # If the user ID already exists, append the new username to the existing document
        users.update_one({"userid":userid}, {"$push": {"username": username}})
    else:
        # If the user ID does not exist, insert a new document into the "users" collection
        users.insert_one({
            "userid": userid,
            "username": [username]
        })



def insert_question(questionid, username):

    # Check if the username already exists in the database
    existing_doc = questions.find_one({"username": username})
    if existing_doc:
        # If the username already exists, append the new question ID to the existing document
        questions.update_one({"username":username}, {"$push": {"questionid": questionid}})
    else:
        # If the username does not exist, insert a new document into the "questions" collection
        questions.insert_one({
            "username": username,
            "questionid": [questionid]
        })



def get_question_ids(userid):  
    # Find all the usernames for the given userid
    usernames = users.find_one({"userid": userid},{"username":1})
    logger.debug(usernames["username"])
    logger.info("") 
    # Iterate over all the usernames
    for username in usernames["username"]:
        # Find all question ids for the given username
        data = get_user_profile(username)
        id = data["data"]["recentAcSubmissionList"][0]["id"]
        questions = users.questions.find_one({"username": username},{"questionid":1})
        length = len(questions["questionid"])-1
        logger.debug(data) 
       
        if(questions["questionid"][length]!=id):
            #Call telegram bot new question is done by the user
            titleSlug = data["data"]["recentAcSubmissionList"][0]["titleSlug"]
            problem_data = get_problem_data(titleSlug)
            logger.info(problem_data)
            print(problem_data)
            res = {
                'chatid':userid,
                'username':username,
                'data':data,
                'question':problem_data["data"]["question"]
            }
            
            return res
        else:
            logger.debug("No new question is done by the %s"% username)
    return None


def get_chat_ids():
    all_docs = users.find({})

    # Create a list to store all the userids
    userids = []

    # Iterate over all the documents in the "users" collection
    for doc in all_docs:
        # Append the "userid" field to the list of userids
        userids.append(doc["userid"])
    
    logger.info(userids)
    return userids
