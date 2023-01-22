import pymongo
from utils import get_user_profile

client = pymongo.MongoClient("mongodb+srv://madhav:madhav@cluster0.i9nlr.mongodb.net/codewithme")


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
    print(usernames["username"])
    # Iterate over all the usernames
    for username in usernames["username"]:
        # Find all question ids for the given username
        data = get_user_profile(username)
        id = data["data"]["recentAcSubmissionList"][0]["id"]
        questions = users.questions.find_one({"username": username},{"questionid":1})
        length = len(questions["questionid"])-1
        if(questions["questionid"][length]!=id):
            #Call telegram bot new question is done by the user
            res = {
                'chatid':userid,
                'username':username,
                'data':data,
            }
            return res
        else:
            print("No new question is done by the %s"% username)
    return None

